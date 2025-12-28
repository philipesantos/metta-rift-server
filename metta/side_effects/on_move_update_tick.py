from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.side_effect import SideEffect


class OnMoveUpdateTick(SideEffect):
    def to_metta_definition(self) -> str:
        out_of_date_tick = OutOfDateTick().to_metta_usage()
        return (
            f"(if (exists {out_of_date_tick})\n"
            f"    Empty\n"
            f"    (add-atom &self {out_of_date_tick})\n"
            f")\n"
        )
