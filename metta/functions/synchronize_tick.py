from metta.atoms.current_tick import CurrentTick
from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.function import Function
from metta.functions.exists import Exists


class SynchronizeTick(Function):
    @staticmethod
    def to_metta_usage() -> str:
        return (
            f"(synchronize-tick)"
        )


    def to_metta_definition(self) -> str:
        current_tick_match = CurrentTick.to_metta_usage("$tick")
        current_tick_remove = CurrentTick.to_metta_usage("$current_tick")
        out_of_date_tick = OutOfDateTick.to_metta_usage()
        current_tick_add = CurrentTick.to_metta_usage("$new_tick")
        return (
            f"(= (synchronize-tick)\n"
            f"    (if {Exists.to_metta_usage(OutOfDateTick.to_metta_usage())}\n"
            f"        (let* (($current_tick (match &self {current_tick_match} $tick))\n"
            f"            ( ()  (remove-atom &self {current_tick_remove}))\n"
            f"            ( ()  (let $new_tick (+ 1 $current_tick) (add-atom &self {current_tick_add})))\n"
            f"            ( ()  (remove-atom &self {out_of_date_tick})))\n"
            f"            Empty\n"
            f"        )\n"
            f"        Empty\n"
            f"    )\n"
            f")"
        )
