from core.patterns.fact_pattern import FactPattern
from utils.type import Type


class ItemFactPattern(FactPattern):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        # fmt: off
        return f"({Type.ITEM.value} {self.key})"
        # fmt: on
