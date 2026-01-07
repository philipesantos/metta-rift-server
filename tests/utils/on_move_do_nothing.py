from metta.definitions.side_effect_definition import SideEffectDefinition


class OnMoveDoNothing(SideEffectDefinition):
    def to_metta(self) -> str:
        return "Empty"
