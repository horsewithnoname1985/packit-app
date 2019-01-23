from .table_elements import TableDataElement
import collections


class SQLCommandGenerator:

    @staticmethod
    def get_update_element_data():
        """
        This method is supposed to update ... continue
        :return:
        """
        pass

    @staticmethod
    def get_add_element_to_table_command(table_name: str, element_id: int,
                                         element: TableDataElement) -> str:

        # TODO: Change SQL command into this:
        # insert into Gender(Name, GenderID) values('male', 1);
        # now:
        # insert into Gender(1, 'male')
        # this is not good because it relies on the proper order of the
        # OrderedDict, the TableDataElement brings. But I want to be able to
        # add new data, that contains more than the TableDataElement data
        # e.g. GarmentTable will hold the Garment object data, which is
        # 'name' and 'gender_id' but the information, whether this garment's
        # quantities must be specified by all new users must also be in it, but
        # it is not part of the Garment object. A new GarmentTable entry is
        # supposed to look like this then:
        # garment_table.add_element(Garment(Name('pants'), GenderID(gender_id)),
        #   QuantityMustBeSpecified(True))
        # so it requires a Garment object and a QuantityMustBeSpecified object

        command = "INSERT INTO " + table_name + ' VALUES(' + str(
            element_id) + ","

        for key in element.fields:
            command += "'" + str(element.fields[key]) + "',"

        command = command[:-1] + ")"

        return command

    @staticmethod
    def get_clean_all_content_command(table_name: str) -> str:
        command = "DELETE FROM " + table_name
        return command

    @staticmethod
    def get_create_table_command(table_name: str,
                                 columns: collections.OrderedDict):
        command = "CREATE TABLE IF NOT EXISTS " + table_name + "("

        for name, kind in columns.items():
            command += name + " " + kind + ", "

        command = command[:-2] + ")"

        return command

    @staticmethod
    def get_remove_element_command(table_name: str,
                                   element: TableDataElement) -> str:

        command = "DELETE FROM " + table_name + " WHERE ("

        for key in element.fields:
            command += key + " = '" + str(element.fields[key]) + "' AND "

        command = command[:-5] + ")"

        return command

    @staticmethod
    def get_return_matching_elements_command(table_name: str,
                                             query_items: dict = None):
        """
        Returns a proper SQL command for selecting matching items of the given
        :param:table_name that are defined by :param:query_items.
        :param: query_items must be of type list where the list items itself
        are dictionaries, containing the column and value of a :param:QueryItem.

        Example:

        get_return_matching_elements_command(table_name="foo", [{foo:bar}, {bar:foo}]

        :param table_name: str
        :param query_items: list of dictionaries
        :return:
        """

        command = "SELECT * FROM " + table_name
        counter = {}

        if query_items:
            for column, value in query_items.items():
                if column not in counter:
                    counter[column] = 1
                else:
                    counter[column] += 1
        else:
            return command

        command = command + " WHERE ("

        for column, value in query_items.items():
            if counter[column] > 1:
                command += column + " = '" + str(value) + "' OR "
                counter[column] -= 1
            elif counter[column] == 1:
                command += column + " = '" + str(value) + "' AND "

        command = command[:-5] + ")"

        return command
