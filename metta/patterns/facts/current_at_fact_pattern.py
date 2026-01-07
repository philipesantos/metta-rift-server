from metta.patterns.fact_pattern import FactPattern
from metta.patterns.pattern import Pattern


class CurrentAtFactPattern(FactPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"(Current At {self.what} {self.where})"
