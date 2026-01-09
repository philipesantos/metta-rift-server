from metta.patterns.fact_pattern import FactPattern


class ItemFactPattern(FactPattern):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        return f"(Item {self.key})"
