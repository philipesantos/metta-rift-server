from metta.definitions.function_definition import FunctionDefinition


class InventoryFunctionPattern(FunctionDefinition):
    def to_metta(self) -> str:
        return (
            f"(= (inventory)\n"
            f"    (match &self (State (At $what player))\n"
            f"        $what\n"
            f"    )\n"
            f")\n"
        )
