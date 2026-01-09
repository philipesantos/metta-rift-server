from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.item_fact_pattern import ItemFactPattern


class ItemFactDefinition(FactDefinition):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        return (
            f"(: {self.key} Item)\n"
            f"{ItemFactPattern(self.key).to_metta()}\n"
        )
