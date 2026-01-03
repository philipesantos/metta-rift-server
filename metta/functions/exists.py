from metta.function import Function


class Exists(Function):
    @staticmethod
    def to_metta_usage(atom: str) -> str:
        return f"(exists {atom})"

    def to_metta_definition(self) -> str:
        return (
            f"(= (exists $atom)\n"
            f"    (let $result\n"
            f"        (collapse (match &self $atom True))\n"
            f"        (case (car-atom $result)\n"
            f"        (\n"
            f"            (True True)\n"
            f"            ($_ False)\n"
            f"        ))\n"
            f"    )\n"
            f")"
        )
