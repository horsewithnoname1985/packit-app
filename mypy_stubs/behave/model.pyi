import six
from behave.matchers import NoMatch as NoMatch
from behave.model_core import BasicStatement as BasicStatement, Replayable as Replayable, Status as Status, TagAndStatusStatement as TagAndStatusStatement, TagStatement as TagStatement
from typing import Any, Optional

class Feature(TagAndStatusStatement, Replayable):
    type: str = ...
    description: Any = ...
    scenarios: Any = ...
    background: Any = ...
    language: Any = ...
    parser: Any = ...
    hook_failed: bool = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, name: Any, tags: Optional[Any] = ..., description: Optional[Any] = ..., scenarios: Optional[Any] = ..., background: Optional[Any] = ..., language: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def __iter__(self) -> Any: ...
    def add_scenario(self, scenario: Any) -> None: ...
    def compute_status(self): ...
    @property
    def duration(self): ...
    def walk_scenarios(self, with_outlines: bool = ...): ...
    def should_run(self, config: Optional[Any] = ...): ...
    def should_run_with_tags(self, tag_expression: Any): ...
    def mark_skipped(self) -> None: ...
    should_skip: bool = ...
    skip_reason: Any = ...
    def skip(self, reason: Optional[Any] = ..., require_not_executed: bool = ...) -> None: ...
    def run(self, runner: Any): ...

class Background(BasicStatement, Replayable):
    type: str = ...
    steps: Any = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, name: Any, steps: Optional[Any] = ...) -> None: ...
    def __iter__(self) -> Any: ...
    @property
    def duration(self): ...

class Scenario(TagAndStatusStatement, Replayable):
    type: str = ...
    continue_after_failed_step: bool = ...
    description: Any = ...
    steps: Any = ...
    background: Any = ...
    feature: Any = ...
    hook_failed: bool = ...
    was_dry_run: bool = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, name: Any, tags: Optional[Any] = ..., steps: Optional[Any] = ..., description: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    @property
    def background_steps(self): ...
    @property
    def all_steps(self): ...
    def __iter__(self) -> Any: ...
    def compute_status(self): ...
    @property
    def duration(self): ...
    @property
    def effective_tags(self): ...
    def should_run(self, config: Optional[Any] = ...): ...
    def should_run_with_tags(self, tag_expression: Any): ...
    def should_run_with_name_select(self, config: Any): ...
    def mark_skipped(self) -> None: ...
    should_skip: bool = ...
    skip_reason: Any = ...
    def skip(self, reason: Optional[Any] = ..., require_not_executed: bool = ...) -> None: ...
    captured: Any = ...
    def run(self, runner: Any): ...

class ScenarioOutlineBuilder:
    annotation_schema: Any = ...
    def __init__(self, annotation_schema: Any) -> None: ...
    @staticmethod
    def render_template(text: Any, row: Optional[Any] = ..., params: Optional[Any] = ...): ...
    name: Any = ...
    index: Any = ...
    id: Any = ...
    def make_scenario_name(self, outline_name: Any, example: Any, row: Any, params: Optional[Any] = ...): ...
    @classmethod
    def make_row_tags(cls, outline_tags: Any, row: Any, params: Optional[Any] = ...): ...
    @classmethod
    def make_step_for_row(cls, outline_step: Any, row: Any, params: Optional[Any] = ...): ...
    def build_scenarios(self, scenario_outline: Any): ...

class ScenarioOutline(Scenario):
    type: str = ...
    annotation_schema: str = ...
    examples: Any = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, name: Any, tags: Optional[Any] = ..., steps: Optional[Any] = ..., examples: Optional[Any] = ..., description: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    @property
    def scenarios(self): ...
    def __iter__(self) -> Any: ...
    def compute_status(self): ...
    @property
    def duration(self): ...
    def should_run_with_tags(self, tag_expression: Any): ...
    def should_run_with_name_select(self, config: Any): ...
    def mark_skipped(self) -> None: ...
    should_skip: bool = ...
    def skip(self, reason: Optional[Any] = ..., require_not_executed: bool = ...) -> None: ...
    def run(self, runner: Any): ...

class Examples(TagStatement, Replayable):
    type: str = ...
    table: Any = ...
    index: Any = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, name: Any, tags: Optional[Any] = ..., table: Optional[Any] = ...) -> None: ...

class Step(BasicStatement, Replayable):
    type: str = ...
    step_type: Any = ...
    text: Any = ...
    table: Any = ...
    status: Any = ...
    hook_failed: bool = ...
    duration: int = ...
    def __init__(self, filename: Any, line: Any, keyword: Any, step_type: Any, name: Any, text: Optional[Any] = ..., table: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def set_values(self, table_row: Any): ...
    captured: Any = ...
    error_message: Any = ...
    def run(self, runner: Any, quiet: bool = ..., capture: bool = ...): ...

class Table(Replayable):
    type: str = ...
    headings: Any = ...
    line: Any = ...
    rows: Any = ...
    def __init__(self, headings: Any, line: Optional[Any] = ..., rows: Optional[Any] = ...) -> None: ...
    def add_row(self, row: Any, line: Optional[Any] = ...) -> None: ...
    def add_column(self, column_name: Any, values: Optional[Any] = ..., default_value: str = ...): ...
    def remove_column(self, column_name: Any) -> None: ...
    def remove_columns(self, column_names: Any) -> None: ...
    def has_column(self, column_name: Any): ...
    def get_column_index(self, column_name: Any): ...
    def require_column(self, column_name: Any): ...
    def require_columns(self, column_names: Any) -> None: ...
    def ensure_column_exists(self, column_name: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, index: Any): ...
    def assert_equals(self, data: Any) -> None: ...

class Row:
    headings: Any = ...
    comments: Any = ...
    cells: Any = ...
    line: Any = ...
    def __init__(self, headings: Any, cells: Any, line: Optional[Any] = ..., comments: Optional[Any] = ...) -> None: ...
    def __getitem__(self, name: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def items(self): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def as_dict(self): ...

class Tag(six.text_type):
    allowed_chars: str = ...
    quoting_chars: Any = ...
    def __new__(cls, name: Any, line: Any): ...
    @classmethod
    def make_name(cls, text: Any, unescape: bool = ..., allowed_chars: Optional[Any] = ...): ...

class Text(six.text_type):
    def __new__(cls, value: Any, content_type: str = ..., line: int = ...): ...
    def line_range(self): ...
    def replace(self, old: Any, new: Any, count: int = ...): ...
    def assert_equals(self, expected: Any): ...

def reset_model(model_elements: Any) -> None: ...
