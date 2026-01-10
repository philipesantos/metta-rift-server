from metta.patterns.function_pattern import FunctionPattern
from metta.patterns.pattern import Pattern


class LocationPathFunctionPattern(FunctionPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        return f"(location-path ({self.what}))"
