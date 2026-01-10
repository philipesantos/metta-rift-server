from core.patterns.event_pattern import EventPattern


class SomeEventPattern(EventPattern):
    def __init__(self, value: str):
        self.value = value

    def to_metta(self) -> str:
        return f"(some event {self.value})"
