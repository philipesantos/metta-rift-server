from metta.functions.function import Function


class Exists(Function):
    @staticmethod
    def to_metta_usage(atom: str) -> str:
        return (
            f"(exists ({atom}))"
        )


    def to_metta_definition(self) -> str:
        return (
            f"(= (exists $atom)\n"
            f"    (case(match &self $atom True)\n"
            f"    (\n"
            f"        (True True)\n"
            f"        (Empty False)\n"
            f"    ))\n"
            f")"
        )
