from metta.functions.function import Function


class CompareNewer(Function):
    @staticmethod
    def to_metta_usage(x_atom: str, y_atom: str) -> str:
        return (
            f"(compare-newer ({x_atom} {y_atom}))"
        )


    def to_metta_definition(self) -> str:
        return (
            f"(= (compare-newer ($x-atom $y-atom))\n"
            f"    (let $x-value (index-atom $x-atom 1)\n"
            f"        (let $y-value (index-atom $y-atom 1)\n"
            f"            (if (> $x-value $y-value) $x-atom $y-atom)\n"
            f"        )\n"
            f"    )\n"
            f")"
        )
