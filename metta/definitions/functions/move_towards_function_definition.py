from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class MoveTowardsFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        state_at_match = StateWrapperPattern(AtFactPattern(self.character.key, "$from"))
        route_match = RouteFactPattern("$from", "$direction", "$to")
        move_event = MoveEventPattern("$from", "$to")
        # fmt: off
        return (
            f"(= (move-towards ($direction))\n"
            f"    (match &self {state_at_match.to_metta()}\n"
            f"        (case (match &self {route_match.to_metta()} $to)\n"
            f"        (\n"
            f'            (Empty "No way to go there")\n'
            f"            ($to {TriggerFunctionPattern(move_event).to_metta()})\n"
            f"        ))\n"
            f"    )\n"
            f")"
        )
        # fmt: on
