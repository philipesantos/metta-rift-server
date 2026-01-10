from metta.definitions.function_definition import FunctionDefinition


class FirstFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(= (first (Cons $x $_))\n"
            f"   $x\n"
            f")"
        )
        # fmt: on
