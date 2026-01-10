from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.item_fact_pattern import ItemFactPattern
from utils.type import Type


class ItemFactDefinition(FactDefinition):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(: {self.key} {Type.ITEM.value})\n"
            f"{ItemFactPattern(self.key).to_metta()}\n"
        )
        # fmt: on
