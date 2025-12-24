from metta.functions.compare_newer import CompareNewer
from metta.functions.function import Function


class Current(Function):
    @staticmethod
    def to_metta_usage(pattern: str) -> str:
        return (
            f"(current ({pattern}))"
        )


    def to_metta_definition(self) -> str:
        compare_newer_metta = CompareNewer.to_metta_usage('$current', '$max')
        return (
            f"(= (current ($pattern))\n"
            f"    (let $eval (collapse (match &self $pattern $pattern))\n"
            f"        (foldl-atom $eval $current $max $current ${compare_newer_metta}))\n"
            f")"
        )

