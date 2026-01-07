from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.function_pattern import FunctionPattern
from metta.patterns.pattern import Pattern


class ExistsFunctionPattern(FunctionPattern):
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def to_metta(self) -> str:
        return f"(exists {self.pattern.to_metta()})"
