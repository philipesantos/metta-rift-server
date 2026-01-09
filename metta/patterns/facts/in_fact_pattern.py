from metta.patterns.fact_pattern import FactPattern


class InFactPattern(FactPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"(In {self.what} {self.where})"
