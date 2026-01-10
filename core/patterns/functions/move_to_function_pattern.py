from core.patterns.function_pattern import FunctionPattern


class MoveToFunctionPattern(FunctionPattern):
    def __init__(self, where: str):
        self.where = where

    def to_metta(self) -> str:
        # fmt: off
        return f"(move-to ({self.where}))"
        # fmt: on
