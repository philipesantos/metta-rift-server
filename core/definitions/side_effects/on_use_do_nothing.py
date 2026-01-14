from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.use_event_pattern import UseEventPattern


class OnUseDoNothing(SideEffectDefinition):
    def to_metta(self, event: UseEventPattern) -> str:
        return "Empty"
