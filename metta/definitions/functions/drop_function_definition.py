from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.events.drop_event_pattern import DropEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.functions.last_function_pattern import LastFunctionPattern
from metta.patterns.functions.location_path_function_pattern import (
    LocationPathFunctionPattern,
)
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class DropFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        state_at_match = StateWrapperPattern(AtFactPattern("$what", "player"))
        location_path = LocationPathFunctionPattern("player")
        last_location = LastFunctionPattern(location_path.to_metta())
        drop_event = DropEventPattern("$what", last_location.to_metta())
        drop_trigger = TriggerFunctionPattern(drop_event)
        return (
            f"(= (drop ($what))\n"
            f"    (match &self {state_at_match.to_metta()}\n"
            f"        {drop_trigger.to_metta()}\n"
            f"    )\n"
            f")"
        )
