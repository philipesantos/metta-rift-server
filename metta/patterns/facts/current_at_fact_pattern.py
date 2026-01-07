from metta.patterns.fact_pattern import FactPattern


class CurrentAtFactPattern(FactPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"(Current At {self.what} {self.where})"
