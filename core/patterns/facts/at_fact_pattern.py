from core.patterns.fact_pattern import FactPattern


class AtFactPattern(FactPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        # fmt: off
        return f"(At {self.what} {self.where})"
        # fmt: on
