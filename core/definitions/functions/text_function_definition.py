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

    def doc_tooltip(self, signature: str) -> str | None:
        return "Builds printable text from nested text fragments."
