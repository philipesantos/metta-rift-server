from metta.definitions.fact_definition import FactDefinition
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.definitions.side_effects.on_move_describe_location import OnMoveDescribeLocation
from metta.patterns.facts.location_fact_pattern import LocationFactPattern


class LocationFactDefinition(FactDefinition):
    def __init__(self, key: str, desc: str):
        self.key = f"{key}"
        self.desc = desc

    def to_metta(self) -> str:
        trigger = TriggerFunctionDefinition(
            MoveEventPattern("$from", self.key), [OnMoveDescribeLocation(self.desc)]
        )
        return (
            f"(: {self.key} Location)\n"
            f"{LocationFactPattern(self.key).to_metta()}\n"
            f"{trigger.to_metta()}"
        )
