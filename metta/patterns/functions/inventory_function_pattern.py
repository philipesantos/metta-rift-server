from metta.patterns.function_pattern import FunctionPattern


class InventoryFunctionPattern(FunctionPattern):
    def to_metta(self) -> str:
        return f"(inventory)"
