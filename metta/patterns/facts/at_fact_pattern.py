from metta.patterns.fact_pattern import FactPattern


class AtFactPattern(FactPattern):
    def __init__(self, tick: str, what: str, where: str):
        self.tick = tick
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"(At {self.tick} {self.what} {self.where})"
