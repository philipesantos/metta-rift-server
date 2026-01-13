from core.definitions.fact_definition import FactDefinition
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.patterns.events.drop_event_pattern import DropEventPattern
from core.patterns.events.pickup_event_pattern import PickUpEventPattern
from core.patterns.facts.item_fact_pattern import ItemFactPattern
from utils.type import Type


class ItemFactDefinition(FactDefinition):
    def __init__(self, key: str, text_pickup: str, text_drop: str):
        self.key = key
        self.text_pickup = text_pickup
        self.text_drop = text_drop

    def to_metta(self) -> str:
        trigger_pickup = TriggerFunctionDefinition(
            PickUpEventPattern(self.key, "$where"), [OnEventPrint(self.text_pickup)]
        )
        trigger_drop = TriggerFunctionDefinition(
            DropEventPattern(self.key, "$where"), [OnEventPrint(self.text_drop)]
        )
        # fmt: off
        return (
            f"(: {self.key} {Type.ITEM.value})\n"
            f"{ItemFactPattern(self.key).to_metta()}\n"
            f"{trigger_pickup.to_metta()}\n"
            f"{trigger_drop.to_metta()}"
        )
        # fmt: on
