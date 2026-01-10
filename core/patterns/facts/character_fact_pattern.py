from core.patterns.fact_pattern import FactPattern
from utils.type import Type


class CharacterFactPattern(FactPattern):
    def __init__(self, key: str, name: str):
        self.key = f"{key}"
        self.name = name

    def to_metta(self) -> str:
        formatted_name = self.name
        if " " in formatted_name:
            formatted_name = f'"{formatted_name}"'
        # fmt: off
        return f"({Type.CHARACTER.value} {self.key} {formatted_name})"
        # fmt: on
