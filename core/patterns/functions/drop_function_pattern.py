from core.patterns.function_pattern import FunctionPattern


class DropFunctionPattern(FunctionPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        # fmt: off
        return f"(drop ({self.what}))"
        # fmt: on
