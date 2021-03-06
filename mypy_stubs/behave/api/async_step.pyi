from typing import Any, Optional

has_asyncio: bool

def async_run_until_complete(astep_func: Optional[Any] = ..., loop: Optional[Any] = ..., timeout: Optional[Any] = ..., async_context: Optional[Any] = ..., should_close: bool = ...): ...
run_until_complete = async_run_until_complete

class AsyncContext:
    default_name: str = ...
    loop: Any = ...
    tasks: Any = ...
    name: Any = ...
    should_close: Any = ...
    def __init__(self, loop: Optional[Any] = ..., name: Optional[Any] = ..., should_close: bool = ..., tasks: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...

def use_or_create_async_context(context: Any, name: Optional[Any] = ..., loop: Optional[Any] = ..., **kwargs: Any): ...
