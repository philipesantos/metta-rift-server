from core.definitions.function_definition import FunctionDefinition


class ExistsFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        # fmt: off
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
        # fmt: on
