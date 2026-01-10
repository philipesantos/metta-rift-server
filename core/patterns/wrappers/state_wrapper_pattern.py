from core.patterns.fact_pattern import FactPattern
from core.patterns.wrapper_pattern import WrapperPattern


class StateWrapperPattern(WrapperPattern):
    def __init__(self, pattern: FactPattern):
        self.pattern = pattern

    def to_metta(self):
        # fmt: off
        return f"(State {self.pattern.to_metta()})"
        # fmt: on
