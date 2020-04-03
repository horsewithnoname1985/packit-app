from behave.textutil import indent as indent
from typing import Any, Optional

def escape_cell(cell: Any): ...
def escape_triple_quotes(text: Any): ...

class ModelDescriptor:
    @staticmethod
    def describe_table(table: Any, indentation: Optional[Any] = ...): ...
    @staticmethod
    def describe_docstring(doc_string: Any, indentation: Optional[Any] = ...): ...

class ModelPrinter(ModelDescriptor):
    stream: Any = ...
    def __init__(self, stream: Any) -> None: ...
    def print_table(self, table: Any, indentation: Optional[Any] = ...) -> None: ...
    def print_docstring(self, text: Any, indentation: Optional[Any] = ...) -> None: ...