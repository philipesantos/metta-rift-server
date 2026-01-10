from core.patterns.event_pattern import EventPattern
from core.patterns.function_pattern import FunctionPattern


class TriggerFunctionPattern(FunctionPattern):
    def __init__(self, event: EventPattern):
        self.event = event

    def to_metta(self) -> str:
        # fmt: off
        return f"(trigger {self.event.to_metta()})"
        # fmt: on
