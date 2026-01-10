from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.event_pattern import EventPattern


class TextSideEffectDefinition(SideEffectDefinition):
    def __init__(self, text: str):
        self.text = text

    def to_metta(self, event: EventPattern) -> str:
        return f'"{self.text}"'
