from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.definitions.side_effects.on_move_describe_location import OnMoveDescribeLocation
from metta.patterns.fact_pattern import FactPattern
from metta.patterns.pattern import Pattern


class LocationFactPattern(FactPattern):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        return f"(Location {self.key})"
