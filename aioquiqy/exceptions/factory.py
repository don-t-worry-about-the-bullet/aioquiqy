import gc
from typing import Optional, Type, Union


class QuiqyAPIError(Exception):
    """Quiqy API Exception"""

    def __init__(
        self,
        code: Optional[int] = None,
        name: Optional[str] = None,
        hint: Optional[str] = None,
    ) -> None:
        self.code = int(code) if code else None
        self.name = name
        self.hint = hint
        super().__init__(self.code)

    @classmethod
    def __call__(
        cls,
        code: Optional[int] = None,
        name: Optional[str] = None,
        hint: Optional[str] = None,
    ) -> Union["QuiqyAPIError", Type["QuiqyAPIError"]]:
        if name and code is not None:
            return cls.exception_to_raise(code, str(name), hint)
        return cls.exception_to_handle(code)

    @classmethod
    def exception_to_handle(cls, code: Optional[int] = None) -> Type["QuiqyAPIError"]:
        if code is None:
            return cls

        catch_exc_classname = cls.generate_exc_classname(code)

        for obj in gc.get_objects():
            if obj.__class__.__name__ == catch_exc_classname:
                return obj.__class__  # type: ignore[return-value,no-any-return]

        return type(catch_exc_classname, (cls,), {})  # type: ignore[return-value]

    @classmethod
    def exception_to_raise(
        cls, code: int, name: str, hint: Optional[str] = None
    ) -> "QuiqyAPIError":
        """Returns an error with error code and error_name"""
        exception_type = type(cls.generate_exc_classname(code), (cls,), {})  # type: ignore
        return exception_type(code, name, hint)  # type: ignore

    @classmethod
    def generate_exc_classname(cls, code: Optional[int]) -> str:
        """Generates unique exception classname based on error code"""
        return f"{cls.__name__}_{code}"

    def __str__(self) -> str:
        hint_text = f" - {self.hint}" if self.hint else ""
        return f"[{self.code}] {self.name}{hint_text}\n"
