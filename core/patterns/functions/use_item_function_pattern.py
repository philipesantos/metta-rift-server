from core.patterns.function_pattern import FunctionPattern


class UseItemFunctionPattern(FunctionPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        # fmt: off
        return f"(use ({self.what}))"
        # fmt: on
