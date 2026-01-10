from metta.patterns.function_pattern import FunctionPattern


class FirstFunctionPattern(FunctionPattern):
    def __init__(self, value: str):
        self.value = value

    def to_metta(self) -> str:
        return f"(first {self.value})"
