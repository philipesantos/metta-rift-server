from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern


class CharacterFactDefinition(FactDefinition):
    def __init__(self, key: str, name: str):
        self.key = f"{key}"
        self.name = name

    def to_pattern(self):
        return CharacterFactPattern(self.key, self.name)

    def to_metta(self) -> str:
        return f"(: {self.key} Character){self.to_pattern().to_metta()}"
