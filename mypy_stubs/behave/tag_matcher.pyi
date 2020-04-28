from typing import Any, Optional

class TagMatcher:
    def should_run_with(self, tags: Any): ...
    def should_exclude_with(self, tags: Any) -> None: ...

class ActiveTagMatcher(TagMatcher):
    value_separator: str = ...
    tag_prefixes: Any = ...
    tag_schema: str = ...
    ignore_unknown_categories: bool = ...
    use_exclude_reason: bool = ...
    value_provider: Any = ...
    tag_pattern: Any = ...
    exclude_reason: Any = ...
    def __init__(self, value_provider: Any, tag_prefixes: Optional[Any] = ..., value_separator: Optional[Any] = ..., ignore_unknown_categories: Optional[Any] = ...) -> None: ...
    @classmethod
    def make_tag_pattern(cls, tag_prefixes: Any, value_separator: Optional[Any] = ...): ...
    @classmethod
    def make_category_tag(cls, category: Any, value: Optional[Any] = ..., tag_prefix: Optional[Any] = ..., value_sep: Optional[Any] = ...): ...
    def is_tag_negated(self, tag: Any): ...
    def is_tag_group_enabled(self, group_category: Any, group_tag_pairs: Any): ...
    def should_exclude_with(self, tags: Any): ...
    def select_active_tags(self, tags: Any) -> None: ...
    def group_active_tags_by_category(self, tags: Any) -> None: ...

class PredicateTagMatcher(TagMatcher):
    predicate: Any = ...
    def __init__(self, exclude_function: Any) -> None: ...
    def should_exclude_with(self, tags: Any): ...

class CompositeTagMatcher(TagMatcher):
    tag_matchers: Any = ...
    def __init__(self, tag_matchers: Optional[Any] = ...) -> None: ...
    def should_exclude_with(self, tags: Any): ...

def setup_active_tag_values(active_tag_values: Any, data: Any) -> None: ...

class OnlyWithCategoryTagMatcher(TagMatcher):
    tag_prefix: str = ...
    value_separator: str = ...
    active_tag: Any = ...
    category_tag_prefix: Any = ...
    def __init__(self, category: Any, value: Any, tag_prefix: Optional[Any] = ..., value_sep: Optional[Any] = ...) -> None: ...
    def should_exclude_with(self, tags: Any): ...
    def select_category_tags(self, tags: Any): ...
    @classmethod
    def make_category_tag(cls, category: Any, value: Optional[Any] = ..., tag_prefix: Optional[Any] = ..., value_sep: Optional[Any] = ...): ...

class OnlyWithAnyCategoryTagMatcher(TagMatcher):
    value_provider: Any = ...
    tag_prefix: Any = ...
    value_separator: Any = ...
    def __init__(self, value_provider: Any, tag_prefix: Optional[Any] = ..., value_sep: Optional[Any] = ...) -> None: ...
    def should_exclude_with(self, tags: Any): ...
    def select_category_tags(self, tags: Any): ...
    def parse_category_tag(self, tag: Any): ...
