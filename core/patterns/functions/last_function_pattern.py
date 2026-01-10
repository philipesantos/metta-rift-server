from core.patterns.function_pattern import FunctionPattern


class LastFunctionPattern(FunctionPattern):
    def __init__(self, value: str):
        self.value = value

    def to_metta(self) -> str:
        # fmt: off
        return f"(last {self.value})"
        # fmt: on
