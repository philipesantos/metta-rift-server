from metta.atoms.tick import Tick
from metta.atoms.wrappers.stale import Stale
from metta.side_effect import SideEffect


class OnMoveUpdateTick(SideEffect):
    def to_metta_definition(self) -> str:
        stale_tick = Stale.to_metta_usage(Tick.__name__)
        return (
            f"(if (exists {stale_tick})\n"
            f"    Empty\n"
            f"    (add-atom &self {stale_tick})\n"
            f")\n"
        )
