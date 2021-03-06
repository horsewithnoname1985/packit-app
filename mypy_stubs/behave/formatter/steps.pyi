from behave import i18n as i18n
from behave.formatter.base import Formatter as Formatter
from behave.step_registry import StepRegistry as StepRegistry, registry as registry
from behave.textutil import compute_words_maxsize as compute_words_maxsize, indent as indent, make_indentation as make_indentation
from typing import Any, Optional

class AbstractStepsFormatter(Formatter):
    step_types: Any = ...
    step_registry: Any = ...
    current_feature: Any = ...
    shows_location: Any = ...
    def __init__(self, stream_opener: Any, config: Any) -> None: ...
    def reset(self) -> None: ...
    def discover_step_definitions(self) -> None: ...
    def feature(self, feature: Any) -> None: ...
    def eof(self) -> None: ...
    stream: Any = ...
    def close(self) -> None: ...
    def report(self) -> None: ...
    def describe_step_definition(self, step_definition: Any, step_type: Optional[Any] = ...): ...

class StepsFormatter(AbstractStepsFormatter):
    name: str = ...
    description: str = ...
    shows_location: bool = ...
    min_location_column: int = ...
    def report(self) -> None: ...
    def report_steps_by_type(self) -> None: ...

class StepsDocFormatter(AbstractStepsFormatter):
    name: str = ...
    description: str = ...
    shows_location: bool = ...
    shows_function_name: bool = ...
    ordered_by_location: bool = ...
    doc_prefix: Any = ...
    def report(self) -> None: ...
    def report_step_definition_docs(self) -> None: ...
    def write_step_definition(self, step_definition: Any) -> None: ...

class StepsCatalogFormatter(StepsDocFormatter):
    name: str = ...
    description: str = ...
    shows_location: bool = ...
    shows_function_name: bool = ...
    ordered_by_location: bool = ...
    doc_prefix: Any = ...
    def describe_step_definition(self, step_definition: Any, step_type: Optional[Any] = ...): ...

class StepsUsageFormatter(AbstractStepsFormatter):
    name: str = ...
    description: str = ...
    doc_prefix: Any = ...
    min_location_column: int = ...
    step_usage_database: Any = ...
    undefined_steps: Any = ...
    def __init__(self, stream_opener: Any, config: Any) -> None: ...
    def reset(self) -> None: ...
    def get_step_type_for_step_definition(self, step_definition: Any): ...
    def select_unused_step_definitions(self): ...
    def update_usage_database(self, step_definition: Any, step: Any) -> None: ...
    def update_usage_database_for_step(self, step: Any) -> None: ...
    def update_usage_database_for_feature(self, feature: Any) -> None: ...
    def feature(self, feature: Any) -> None: ...
    def report(self) -> None: ...
    def report_used_step_definitions(self): ...
    def report_unused_step_definitions(self): ...
    def report_undefined_steps(self) -> None: ...

def steps_contain(steps: Any, step: Any): ...
