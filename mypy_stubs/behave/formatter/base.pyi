from behave.textutil import select_best_encoding as select_best_encoding
from typing import Any, Optional

class StreamOpener:
    default_encoding: Any = ...
    name: Any = ...
    stream: Any = ...
    encoding: Any = ...
    should_close_stream: Any = ...
    def __init__(self, filename: Optional[Any] = ..., stream: Optional[Any] = ..., encoding: Optional[Any] = ...) -> None: ...
    @staticmethod
    def ensure_dir_exists(directory: Any) -> None: ...
    @classmethod
    def ensure_stream_with_encoder(cls, stream: Any, encoding: Optional[Any] = ...): ...
    def open(self): ...
    def close(self): ...

class Formatter:
    name: Any = ...
    description: Any = ...
    stream_opener: Any = ...
    stream: Any = ...
    config: Any = ...
    def __init__(self, stream_opener: Any, config: Any) -> None: ...
    @property
    def stdout_mode(self): ...
    def open(self): ...
    def uri(self, uri: Any) -> None: ...
    def feature(self, feature: Any) -> None: ...
    def background(self, background: Any) -> None: ...
    def scenario(self, scenario: Any) -> None: ...
    def step(self, step: Any) -> None: ...
    def match(self, match: Any) -> None: ...
    def result(self, step: Any) -> None: ...
    def eof(self) -> None: ...
    def close(self) -> None: ...
    def close_stream(self) -> None: ...
