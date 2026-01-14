from core.patterns.function_pattern import FunctionPattern


class UseFunctionPattern(FunctionPattern):
    def __init__(self, what: str, with_what: str):
        self.what = what
        self.with_what = with_what

    def to_metta(self) -> str:
        # fmt: off
        return f"(use ({self.what} {self.with_what}))"
        # fmt: on
