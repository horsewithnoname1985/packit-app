from packit_app.table_elements import TableDataElement
from packit_app.table_fields import TableField

import collections
from typing import Union


class SQLCommandGenerator:

    @staticmethod
    def get_add_element_to_table_command(table_name: str, element_id: int,
                                         element: TableDataElement) -> str:

        command = "INSERT INTO " + table_name + ' VALUES(' + str(
                element_id) + ","

        for key, value in element.column_types.items():
            if isinstance(key, TableField):
                value = value.get_value()
            command += "'" + str(value) + "',"

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

        for key in element.column_types:
            command += key + " = '" + str(element.column_types[key]) + "' AND "

        command = command[:-5] + ")"

        return command

    @staticmethod
    def get_return_matching_elements_command(
            table_name: str, query_items: collections.OrderedDict = None):
        """
        Returns a proper SQL command for selecting matching items of the given
        :param:table_name that are defined by :param:query_items.
        :param: query_items must be of type list where the list items itself
        are dictionaries, containing the column and value of a
        :param:QueryItem.

        Example:

        get_return_matching_elements_command(table_name="foo", [{foo:bar},
        {bar:foo}]

        :param table_name: str
        :param query_items: list of dictionaries
        :return: command: str
        """

        command = "SELECT * FROM " + table_name
        counter: dict = {}

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

    @staticmethod
    def get_update_single_value_command(table,
                                        element_id: int,
                                        field: str,
                                        value: Union[int, float]):

        command = f"UPDATE {table.table_name} SET {field} = {value} WHERE " \
                  f"{table.primary_key_column_name} = {element_id}"

        return command
