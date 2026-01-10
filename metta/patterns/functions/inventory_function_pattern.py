from metta.patterns.function_pattern import FunctionPattern


class InventoryFunctionPattern(FunctionPattern):
    def to_metta(self) -> str:
        # fmt: off
        return f"(inventory)"
        # fmt: on
