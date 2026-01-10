from core.patterns.function_pattern import FunctionPattern
from core.patterns.pattern import Pattern


class ExistsFunctionPattern(FunctionPattern):
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def to_metta(self) -> str:
        # fmt: off
        return f"(exists {self.pattern.to_metta()})"
        # fmt: on
