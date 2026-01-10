from metta.patterns.event_pattern import EventPattern
from metta.patterns.wrapper_pattern import WrapperPattern


class LogWrapperPattern(WrapperPattern):
    def __init__(self, tick: str, pattern: EventPattern):
        self.tick = tick
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return f"(Log {self.tick} {self.pattern.to_metta()})"
        # fmt: on
