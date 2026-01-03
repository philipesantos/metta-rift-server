from metta.side_effect import SideEffect


class OnMoveDoNothing(SideEffect):
    def to_metta_definition(self) -> str:
        return "Empty"
