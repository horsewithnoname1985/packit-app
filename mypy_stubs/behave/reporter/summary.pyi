from behave.formatter.base import StreamOpener as StreamOpener
from behave.model import ScenarioOutline as ScenarioOutline
from behave.model_core import Status as Status
from behave.reporter.base import Reporter as Reporter
from typing import Any

optional_steps: Any
status_order: Any

def format_summary(statement_type: Any, summary: Any): ...

class SummaryReporter(Reporter):
    show_failed_scenarios: bool = ...
    output_stream_name: str = ...
    stream: Any = ...
    feature_summary: Any = ...
    scenario_summary: Any = ...
    step_summary: Any = ...
    duration: float = ...
    failed_scenarios: Any = ...
    def __init__(self, config: Any) -> None: ...
    def feature(self, feature: Any) -> None: ...
    def end(self) -> None: ...
    def process_scenario(self, scenario: Any) -> None: ...
    def process_scenario_outline(self, scenario_outline: Any) -> None: ...
