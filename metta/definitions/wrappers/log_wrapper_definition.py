from metta.definitions.wrapper_definition import WrapperDefinition
from metta.patterns.fact_pattern import FactPattern
from metta.patterns.wrapper_pattern import WrapperPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern


class LogWrapperDefinition(WrapperDefinition):
    def __init__(self, tick: str, pattern: FactPattern):
        self.tick = tick
        self.pattern = pattern

    def to_metta(self):
        return LogWrapperPattern(self.tick, self.pattern).to_metta()
