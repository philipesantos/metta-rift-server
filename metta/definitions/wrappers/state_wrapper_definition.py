from metta.definitions.wrapper_definition import WrapperDefinition
from metta.patterns.fact_pattern import FactPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class StateWrapperDefinition(WrapperDefinition):
    def __init__(self, pattern: FactPattern):
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return StateWrapperPattern(self.pattern).to_metta()
        # fmt: on
