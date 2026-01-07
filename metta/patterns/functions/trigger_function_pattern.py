from metta.patterns.event_pattern import EventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.side_effect_definition import SideEffectDefinition
from metta.patterns.function_pattern import FunctionPattern


class TriggerFunctionPattern(FunctionPattern):
    def __init__(self, event: EventPattern):
        self.event = event

    def to_metta(self) -> str:
        return f"(trigger {self.event.to_metta()})"
