from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.side_effect import SideEffect


class OnMoveUpdateTickSideEffect(SideEffect):
    def to_metta_definition(self) -> str:
        out_of_date_tick = OutOfDateTick().to_metta_usage()
        return (
            f"(add-atom &self {out_of_date_tick})\n"
        )
