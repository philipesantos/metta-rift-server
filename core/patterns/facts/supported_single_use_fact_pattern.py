from core.patterns.fact_pattern import FactPattern


class SupportedSingleUseFactPattern(FactPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        # fmt: off
        return f"(SupportedSingleUse {self.what})"
        # fmt: on
