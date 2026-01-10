from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from utils.type import Type


class CharacterFactDefinition(FactDefinition):
    def __init__(self, key: str, name: str):
        self.key = f"{key}"
        self.name = name

    def to_pattern(self):
        return CharacterFactPattern(self.key, self.name)

    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(: {self.key} {Type.CHARACTER.value})"
            f"{self.to_pattern().to_metta()}"
        )
        # fmt: on
