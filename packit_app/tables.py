from collections import OrderedDict
from abc import ABC, abstractmethod
from sqlite3 import Error
from typing import Union

from packit_app.errors import AmbiguousElementError, \
    ElementAlreadyExistsError, ElementNotFoundError, UnkownTableTypeError
from packit_app.sql_command_generator import SQLCommandGenerator as Cmd
from packit_app.table_elements import TableDataElement, Gender, Male, Female, \
    User, Garment, UserGarmentSetting, Trip, UserTripGarmentAmount
from packit_app.table_fields import TableField, UserGarmentSettingsID, \
    UserID, TableIdentifierField, TableDataField
from packit_app.table_helper import TableHelper


class Table:
    """
    Parent class for all tables inside the database.

    .. warning::
        Please do not create tables by instantiating this class, but use the
        `TableFactoryImpl.create_table()` method for this purpose.

    Each table requires a `primary_key` column, which saves an integer value
    for each `TableDataElement` that is added to the table.

    :param primary_key_column_name: string name that the primary key column
        is supposed to have.
    :param column_types: dictionary that holds a key-value pair for each column
        , where the key holds the column name and the value contains the type
        information.
    """
    helper = TableHelper()
    table_name = ""
    primary_key_column_name = ""
    id = 1
    raised_errors: list = []

    def __init__(self, db, primary_key_column_name: str, column_types) -> None:
        self.db = db
        column_types.update(
                {primary_key_column_name: "INTEGER NOT NULL PRIMARY KEY ASC"})
        column_types.move_to_end(primary_key_column_name, last=False)
        self.db.execute_command(Cmd.get_create_table_command(self.table_name,
                                                             column_types))

    def _element_already_exists(self, element: TableDataElement):
        """Checks whether the table already contains an element with the same
        data. Raises an ElementAlreadyExistsError in case the element already
        exists."""

        self.db.execute_command(Cmd.get_return_matching_elements_command(
                self.table_name, element.get_as_dict()))

        data = self.db.cur.fetchall()
        if len(data) == 0:
            return False
        else:
            raise ElementAlreadyExistsError

    def add_element(self, element: TableDataElement):
        """
        Adds a single `TableDataElement` to the table.

        :param element: element to be added
        :return: None
        """

        try:
            if not self._element_already_exists(element):
                self.db.execute_command(Cmd.get_add_element_to_table_command(
                        self.table_name,
                        self.id,
                        element))
                self.id += 1
                return self.id - 1

        except ElementAlreadyExistsError as error:
            self.raised_errors.append(error)
            # TODO: Handle error with warning pop-up message

    def clean_all_content(self):
        """
        Removes all data from the table. Column types are not removed.

        :return: None
        """
        command = Cmd.get_clean_all_content_command(self.table_name)
        self.db.cur.execute(command)
        self.id = 1

    def delete_element(self, element: TableDataElement):
        """
        Removes a single data `TableDataElement` from the table.

        :param element: `TableDataElement` that is supposed to be removed from
            the table.
        :return: None
        """

        command = Cmd.get_remove_element_command(
                self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_matching_element(self, element: TableDataElement):
        """
        Returns matching TableDataElement data as dictionary

        Since a table only contains unique elements, only one element that will
        be searched for is allowed to be passed.

        Example:
        ```Table.get_matching_element(User(Username("Freddy"), Male())``

        :param element: A single object of type TableDataElement
        :rtype: single dictionary, containing all field data for this element.
            An empty dictionary is returned in case no match is found
        """

        command = Cmd.get_return_matching_elements_command(
                self.table_name, element.get_as_dict())

        return self.helper.get_row_content_as_dictionary(
                self.db.cur.execute(command))

    def get_matching_elements(self, *field_values: TableField):
        """
        Returns all matching table elements as a list dictionaries.

        `TableField`
        Zero, one or more dictionaries of type
        :class:`~packit_app.field_values.TableField` can to be passed as
        ``field_values``. If none are passed, all table elements are returned.
        Any passed ``field_value`` argument functions as a filter, where only
        elements fulfilling all filter conditions are returned.

        Example:
        ``Table.get_matching_elements(Username('Freddy')), Male()`` returns all
        entries of the table that have the username 'Freddy' and is of gender
        `Male`.

        :param field_values: Zero, one or more `TableField` objects
        :rtype: list of dictionaries, if one or more elements are found. Each
            dictionary contains the complete data of each matching
            `TableDataElement`. An empty list is returned in case no match is
            found.
        """

        all_queries_dict: OrderedDict = OrderedDict()
        for field_value in field_values:
            all_queries_dict.update(field_value.get_as_dict())

        command = Cmd.get_return_matching_elements_command(
                self.table_name, all_queries_dict)

        result = [r for r in
                  self.helper.get_cursor_data_as_dictionary_generator(
                          self.db.cur.execute(command))]

        return result

    def get_matching_primary_key(self, *field_values: TableField):
        """
        This
        :arg field_values: One or more objects of type `FieldValue` needed
        to identify a single table entry. If more than one element matches
        passed ``field_values`` parameters an `AmbiguousElementError`

        :rtype: single element id as 'int'.
        """
        element = self.get_matching_elements(*field_values)
        if len(element) > 1:
            raise AmbiguousElementError
        if len(element) == 0:
            raise ElementNotFoundError
        else:
            return element[self.primary_key_column_name]

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors

    def get_primary_key(self, *fields: TableField):

        result = self.get_matching_elements(*fields)

        if len(result) == 1:
            return result[0][self.primary_key_column_name]
        elif len(result) > 1:
            raise Error("Query matches multiple elements")
        else:
            return

    def set_data(self, element_id: TableIdentifierField,
                 data_field: TableDataField,
                 value: Union[int, float]) -> None:
        """
        Sets a `value` for a `data_field` for the table entry with the
        specified `primary_key`. Returns a `DatabaseError` if either the
        `primary_key` or the `data_field` does not exists. Returns a
        `TypeError` if the `value` is not of the correct type.
        :param element_id: `TableIdentifierField` which contains the/a unique
        identifying value for this element (best: use primary key field)
        :param data_field: `TableDataField` object representing the data field
        that is updated
        :param value: New value (either of type `int` or `float`)
        :return: None
        """

        command = Cmd.get_update_single_value_command(self,
                                                      element_id.column_name,
                                                      data_field.column_name,
                                                      value)
        self.db.cur.execute(command)
        self.db.connection.commit()


class GarmentTable(Table):
    table_name = "Garment"
    primary_key_column_name = "GarmentID"

    def __init__(self, database, column_types: OrderedDict):
        super(GarmentTable, self).__init__(database,
                                           self.primary_key_column_name,
                                           column_types)


class GenderTable(Table):
    table_name = "Gender"
    primary_key_column_name = "GenderID"

    MaleID, FemaleID = 0, 0

    def __init__(self, database, column_types):
        super(GenderTable, self).__init__(database,
                                          self.primary_key_column_name,
                                          column_types)
        self.MaleID = super(GenderTable, self).add_element(Male())
        self.FemaleID = super(GenderTable, self).add_element(Female())


class TripTable(Table):
    table_name = "Trip"
    primary_key_column_name = "TripID"

    def __init__(self, database, columns: OrderedDict):
        super(TripTable, self).__init__(database, self.primary_key_column_name,
                                        columns)


class UserGarmentSettingsTable(Table):
    """
    UserSettingsTable contains the individual settings of each user. It
    implements the TableStrategy interface.
    """
    table_name = "UserGarmentSettings"
    primary_key_column_name = UserGarmentSettingsID.column_name

    def __init__(self, database, columns: OrderedDict):
        super(UserGarmentSettingsTable, self).__init__(
                database,
                self.primary_key_column_name,
                columns)


class UserTable(Table):
    """
    UserTable manages the packit 'users' table within the Database which
    manages the registered users. It implements the TableStrategy interface.
    """

    table_name = 'User'
    primary_key_column_name = UserID.column_name

    def __init__(self, database, column_types):
        super(UserTable, self).__init__(database, self.primary_key_column_name,
                                        column_types)


class UserTripGarmentAmountTable(Table):
    table_name = "UserTripGarmentAmount"
    primary_key_column_name = "UserTripGarmentAmountID"

    def __init__(self, database, columns: OrderedDict):
        super(UserTripGarmentAmountTable, self).__init__(
                database,
                self.primary_key_column_name,
                columns)


class TableFactory(ABC):
    """Abstract class that all table factory classes must implement"""

    def __init__(self):
        self.column_types = OrderedDict()

    @abstractmethod
    def create_table(self, element: TableDataElement):
        pass


class TableFactoryImpl(TableFactory):
    """The sole purpose of this class is to create `Table` objects."""

    def __init__(self, database):
        super(TableFactoryImpl, self).__init__()
        self.database = database

    def create_table(self, element: TableDataElement) -> Table:
        """Creates a Table object inside a :class:`Database` object.

        Item must be an implementation of the `TableDataElement` interface,
        which defines the resulting type of the table, that is returned.
        The proper column types are assigned to the table, depending on the
        default input value of each `TableField`, that `item` contains.
        The column names are derived accordingly.

        :param element: defines the element type the table is supposed to
         store. Must be of type `TableDataElement`.
        :rtype: `Table`
        """
        self.column_types.clear()

        for column in element.column_types:
            if type(element.column_types[column]) == str:
                self.column_types[column] = "TEXT"
            elif isinstance(element.column_types[column], (int, bool)):
                self.column_types[column] = "INTEGER"
            elif type(element.column_types[column]) == float:
                self.column_types[column] = "REAL"

        if isinstance(element, User):
            return UserTable(self.database, self.column_types)
        elif isinstance(element, Gender):
            return GenderTable(self.database, self.column_types)
        elif isinstance(element, Garment):
            return GarmentTable(self.database, self.column_types)
        elif isinstance(element, UserGarmentSetting):
            return UserGarmentSettingsTable(self.database, self.column_types)
        elif isinstance(element, Trip):
            return TripTable(self.database, self.column_types)
        elif isinstance(element, UserTripGarmentAmount):
            return UserTripGarmentAmountTable(self.database, self.column_types)
        else:
            raise UnkownTableTypeError
