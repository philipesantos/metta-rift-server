from metta.definitions.side_effect_definition import SideEffectDefinition
from metta.patterns.events.move_event_pattern import MoveEventPattern


class OnMoveDoNothing(SideEffectDefinition):
    def to_metta(self, event: MoveEventPattern) -> str:
        return "Empty"
