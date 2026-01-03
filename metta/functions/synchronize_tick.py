from metta.atoms.wrappers.stale import Stale
from metta.atoms.wrappers.state import State
from metta.atoms.tick import Tick
from metta.function import Function
from metta.functions.exists import Exists


class SynchronizeTick(Function):
    @staticmethod
    def to_metta_usage() -> str:
        return f"(synchronize-tick)"

    def to_metta_definition(self) -> str:
        stale_tick = Stale.to_metta_usage(Tick.__name__)
        tick_state_match = State.to_metta_usage(Tick.to_metta_usage("$tick"))
        tick_state_remove = State.to_metta_usage(Tick.to_metta_usage("$current_tick"))
        tick_state_add = State.to_metta_usage(Tick.to_metta_usage("$new_tick"))
        return (
            f"(= (synchronize-tick)\n"
            f"    (if {Exists.to_metta_usage(stale_tick)}\n"
            f"        (let* (($current_tick (match &self {tick_state_match} $tick))\n"
            f"            ( ()  (remove-atom &self {tick_state_remove}))\n"
            f"            ( ()  (let $new_tick (+ 1 $current_tick) (add-atom &self {tick_state_add})))\n"
            f"            ( ()  (remove-atom &self {stale_tick})))\n"
            f"            Empty\n"
            f"        )\n"
            f"        Empty\n"
            f"    )\n"
            f")"
        )
