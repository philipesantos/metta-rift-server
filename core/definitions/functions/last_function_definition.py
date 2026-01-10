from core.definitions.function_definition import FunctionDefinition


class LastFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(= (last (Cons $x (Nil)))\n"
            f"   $x\n"
            f")\n\n"
            f"(= (last (Cons $_ (Cons $y $tail)))\n"
            f"   (last (Cons $y $tail))\n"
            f")"
        )
        # fmt: on
