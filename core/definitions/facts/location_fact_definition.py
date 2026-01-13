from core.definitions.fact_definition import FactDefinition
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.patterns.facts.location_fact_pattern import LocationFactPattern
from utils.type import Type


class LocationFactDefinition(FactDefinition):
    def __init__(self, key: str, text_move_to: str):
        self.key = f"{key}"
        self.text_move_to = text_move_to

    def to_metta(self) -> str:
        trigger_move_to = TriggerFunctionDefinition(
            MoveEventPattern("$from", self.key), [OnEventPrint(self.text_move_to)]
        )
        # fmt: off
        return (
            f"(: {self.key} {Type.LOCATION.value})\n"
            f"{LocationFactPattern(self.key).to_metta()}\n"
            f"{trigger_move_to.to_metta()}"
        )
        # fmt: on
