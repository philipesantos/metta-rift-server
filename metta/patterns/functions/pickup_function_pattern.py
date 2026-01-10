from metta.patterns.function_pattern import FunctionPattern


class PickUpFunctionPattern(FunctionPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        return f"(pickup ({self.what}))"
