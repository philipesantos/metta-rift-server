from core.definitions.fact_definition import FactDefinition
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_move_describe_location import (
    OnMoveDescribeLocation,
)
from core.patterns.facts.location_fact_pattern import LocationFactPattern
from utils.type import Type


class LocationFactDefinition(FactDefinition):
    def __init__(self, key: str, desc: str):
        self.key = f"{key}"
        self.desc = desc

    def to_metta(self) -> str:
        trigger = TriggerFunctionDefinition(
            MoveEventPattern("$from", self.key), [OnMoveDescribeLocation(self.desc)]
        )
        # fmt: off
        return (
            f"(: {self.key} {Type.LOCATION.value})\n"
            f"{LocationFactPattern(self.key).to_metta()}\n"
            f"{trigger.to_metta()}"
        )
        # fmt: on
