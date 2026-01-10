from metta.definitions.function_definition import FunctionDefinition


class LastFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        return (
            f"(= (last (Cons $x (Nil)))\n"
            f"   $x\n"
            f")\n"
            f"(= (last (Cons $_ (Cons $y $tail)))\n"
            f"   (last (Cons $y $tail))\n"
            f")"
        )
