import gc
from typing import Optional, Type, Union

class QuiqyAPIError(Exception):
    code: Optional[int]
    name: Optional[str]
    hint: Optional[str]
    
    def __init__(
        self,
        code: Optional[int] = None,
        name: Optional[str] = None,
        hint: Optional[str] = None,
    ) -> None: ...
    
    @classmethod
    def __call__(
        cls,
        code: Optional[int] = None,
        name: Optional[str] = None,
        hint: Optional[str] = None,
    ) -> Union["QuiqyAPIError", Type["QuiqyAPIError"]]: ...
    
    @classmethod
    def exception_to_handle(cls, code: Optional[int] = None) -> Type["QuiqyAPIError"]: ...
    
    @classmethod
    def exception_to_raise(
        cls, code: int, name: str, hint: Optional[str] = None
    ) -> "QuiqyAPIError": ...
    
    @classmethod
    def generate_exc_classname(cls, code: Optional[int]) -> str: ...
    
    def __str__(self) -> str: ...
