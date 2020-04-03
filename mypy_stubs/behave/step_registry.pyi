from typing import Any

class AmbiguousStep(ValueError): ...

class StepRegistry:
    steps: Any = ...
    def __init__(self) -> None: ...
    @staticmethod
    def same_step_definition(step: Any, other_pattern: Any, other_location: Any): ...
    def add_step_definition(self, keyword: Any, step_text: Any, func: Any) -> None: ...
    def find_step_definition(self, step: Any): ...
    def find_match(self, step: Any): ...
    def make_decorator(self, step_type: Any): ...

# Names in __all__ with no definition:
#   Given
#   Step
#   Then
#   When
#   given
#   step
#   then
#   when