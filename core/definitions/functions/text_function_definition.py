from core.definitions.function_definition import FunctionDefinition


class TextFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(= (Text $x)\n"
            f"   $x\n"
            f")"
        )
        # fmt: on
