from metta.atoms.tick import Tick
from metta.functions.function import Function


class CurrentTick(Function):
    @staticmethod
    def to_metta_usage() -> str:
        return (
            f"(current-tick)"
        )


    def to_metta_definition(self) -> str:
        tick_metta = Tick.to_metta_usage("$tick")
        return (
            f"(= (current-tick)\n"
            f"    (let $current-tick (current (${tick_metta}))\n"
            f"        (index-atom $current-tick 1)\n"
            f"    )\n"
            f")"
        )
