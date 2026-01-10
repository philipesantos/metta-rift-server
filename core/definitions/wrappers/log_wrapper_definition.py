from core.definitions.wrapper_definition import WrapperDefinition
from core.patterns.event_pattern import EventPattern
from core.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern


class LogWrapperDefinition(WrapperDefinition):
    def __init__(self, tick: str, pattern: EventPattern):
        self.tick = tick
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return LogWrapperPattern(self.tick, self.pattern).to_metta()
        # fmt: on
