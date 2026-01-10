from core.definitions.wrapper_definition import WrapperDefinition
from core.patterns.fact_pattern import FactPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class StateWrapperDefinition(WrapperDefinition):
    def __init__(self, pattern: FactPattern):
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return StateWrapperPattern(self.pattern).to_metta()
        # fmt: on
