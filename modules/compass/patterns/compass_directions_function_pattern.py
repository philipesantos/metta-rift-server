from core.patterns.function_pattern import FunctionPattern


class CompassDirectionsFunctionPattern(FunctionPattern):
    def __init__(self, location: str):
        self.location = location

    def to_metta(self) -> str:
        # fmt: off
        return f"(compass-directions ({self.location}))"
        # fmt: on
