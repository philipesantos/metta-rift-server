from metta.patterns.fact_pattern import FactPattern
from metta.patterns.wrapper_pattern import WrapperPattern


class LogWrapperPattern(WrapperPattern):
    def __init__(self, tick: str, atom: FactPattern):
        self.tick = tick
        self.atom = atom

    def to_metta(self):
        return f"(Log {self.tick} {self.atom.to_metta()})"
