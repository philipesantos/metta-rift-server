from metta.patterns.function_pattern import FunctionPattern


class SynchronizeTickFunctionPattern(FunctionPattern):
    def to_metta(self) -> str:
        return f"(synchronize-tick)"
