from metta.definitions.wrapper_definition import WrapperDefinition
from metta.patterns.event_pattern import EventPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern


class LogWrapperDefinition(WrapperDefinition):
    def __init__(self, tick: str, pattern: EventPattern):
        self.tick = tick
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return LogWrapperPattern(self.tick, self.pattern).to_metta()
        # fmt: on
