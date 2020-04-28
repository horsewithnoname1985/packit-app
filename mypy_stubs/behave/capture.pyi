from behave.log_capture import LoggingCapture as LoggingCapture
from typing import Any, Optional

def add_text_to(value: Any, more_text: Any, separator: str = ...): ...

class Captured:
    empty: str = ...
    linesep: str = ...
    stdout: Any = ...
    stderr: Any = ...
    log_output: Any = ...
    def __init__(self, stdout: Optional[Any] = ..., stderr: Optional[Any] = ..., log_output: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def __bool__(self): ...
    @property
    def output(self): ...
    def add(self, captured: Any): ...
    def make_report(self): ...
    def __add__(self, other: Any): ...
    def __iadd__(self, other: Any): ...

class CaptureController:
    config: Any = ...
    stdout_capture: Any = ...
    stderr_capture: Any = ...
    log_capture: Any = ...
    old_stdout: Any = ...
    old_stderr: Any = ...
    def __init__(self, config: Any) -> None: ...
    @property
    def captured(self): ...
    def setup_capture(self, context: Any) -> None: ...
    def start_capture(self) -> None: ...
    def stop_capture(self) -> None: ...
    def teardown_capture(self) -> None: ...
    def make_capture_report(self): ...

def capture_output(controller: Any, enabled: bool = ...) -> None: ...
