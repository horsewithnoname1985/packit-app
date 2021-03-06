from behave._types import ChainedExceptionUtil as ChainedExceptionUtil, ExceptionUtil as ExceptionUtil
from behave.model_core import Argument as Argument, FileLocation as FileLocation, Replayable as Replayable
from typing import Any, Optional

class StepParseError(ValueError):
    def __init__(self, text: Optional[Any] = ..., exc_cause: Optional[Any] = ...) -> None: ...

class Match(Replayable):
    type: str = ...
    func: Any = ...
    arguments: Any = ...
    location: Any = ...
    def __init__(self, func: Any, arguments: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def with_arguments(self, arguments: Any): ...
    def run(self, context: Any) -> None: ...
    @staticmethod
    def make_location(step_function: Any): ...

class NoMatch(Match):
    func: Any = ...
    arguments: Any = ...
    location: Any = ...
    def __init__(self) -> None: ...

class MatchWithError(Match):
    stored_error: Any = ...
    def __init__(self, func: Any, error: Any) -> None: ...
    def run(self, context: Any) -> None: ...

class Matcher:
    schema: str = ...
    func: Any = ...
    pattern: Any = ...
    step_type: Any = ...
    def __init__(self, func: Any, pattern: Any, step_type: Optional[Any] = ...) -> None: ...
    @property
    def string(self): ...
    @property
    def location(self): ...
    @property
    def regex_pattern(self): ...
    def describe(self, schema: Optional[Any] = ...): ...
    def check_match(self, step: Any) -> None: ...
    def match(self, step: Any): ...

class ParseMatcher(Matcher):
    custom_types: Any = ...
    parser_class: Any = ...
    parser: Any = ...
    def __init__(self, func: Any, pattern: Any, step_type: Optional[Any] = ...) -> None: ...
    @property
    def regex_pattern(self): ...
    def check_match(self, step: Any): ...

class CFParseMatcher(ParseMatcher):
    parser_class: Any = ...

def register_type(**kw: Any) -> None: ...

class RegexMatcher(Matcher):
    regex: Any = ...
    def __init__(self, func: Any, pattern: Any, step_type: Optional[Any] = ...) -> None: ...
    def check_match(self, step: Any): ...

class SimplifiedRegexMatcher(RegexMatcher):
    pattern: Any = ...
    def __init__(self, func: Any, pattern: Any, step_type: Optional[Any] = ...) -> None: ...

class CucumberRegexMatcher(RegexMatcher): ...

matcher_mapping: Any
current_matcher = ParseMatcher

def use_step_matcher(name: Any) -> None: ...
def step_matcher(name: Any) -> None: ...
def get_matcher(func: Any, pattern: Any): ...
