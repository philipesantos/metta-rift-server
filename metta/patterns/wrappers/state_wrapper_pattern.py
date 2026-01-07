from metta.patterns.fact_pattern import FactPattern
from metta.patterns.wrapper_pattern import WrapperPattern


class StateWrapperPattern(WrapperPattern):
    def __init__(self, pattern: FactPattern):
        self.pattern = pattern

    def to_metta(self):
        return f"(State {self.pattern.to_metta()})"
