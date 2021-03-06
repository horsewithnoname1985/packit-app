from behave.formatter.base import Formatter as Formatter
from behave.model_core import Status as Status
from typing import Any

class ProgressFormatterBase(Formatter):
    dot_status: Any = ...
    show_timings: bool = ...
    stream: Any = ...
    steps: Any = ...
    failures: Any = ...
    current_feature: Any = ...
    current_scenario: Any = ...
    def __init__(self, stream_opener: Any, config: Any) -> None: ...
    def reset(self) -> None: ...
    def feature(self, feature: Any) -> None: ...
    def background(self, background: Any) -> None: ...
    def scenario(self, scenario: Any) -> None: ...
    def step(self, step: Any) -> None: ...
    def result(self, step: Any) -> None: ...
    def eof(self) -> None: ...
    def report_step_progress(self, step: Any) -> None: ...
    def report_scenario_progress(self) -> None: ...
    def report_feature_completed(self) -> None: ...
    def report_scenario_completed(self) -> None: ...
    def report_feature_duration(self) -> None: ...
    def report_scenario_duration(self) -> None: ...
    def report_failures(self) -> None: ...

class ScenarioProgressFormatter(ProgressFormatterBase):
    name: str = ...
    description: str = ...
    def report_scenario_progress(self) -> None: ...
    def report_feature_completed(self) -> None: ...

class StepProgressFormatter(ProgressFormatterBase):
    name: str = ...
    description: str = ...
    def report_step_progress(self, step: Any) -> None: ...
    def report_feature_completed(self) -> None: ...

class ScenarioStepProgressFormatter(StepProgressFormatter):
    name: str = ...
    description: str = ...
    indent_size: int = ...
    scenario_prefix: Any = ...
    current_feature: Any = ...
    def feature(self, feature: Any) -> None: ...
    current_scenario: Any = ...
    def scenario(self, scenario: Any) -> None: ...
    def report_feature_completed(self) -> None: ...
    failures: Any = ...
    def report_scenario_completed(self) -> None: ...
    def report_failures(self) -> None: ...
