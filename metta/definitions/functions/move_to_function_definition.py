from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern


class MoveToFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        current_at_match = CurrentAtFactPattern(self.character.key, "$from")
        log_move_event_match = LogWrapperPattern("$tick", MoveEventPattern("$_", "$to"))
        move_event_trigger = MoveEventPattern("$from", "$to")
        return (
            f"(= (move-to ($to))\n"
            f"    (match &self {current_at_match.to_metta()}\n"
            f"        (if {ExistsFunctionPattern(log_move_event_match).to_metta()}\n"
            f"            {TriggerFunctionPattern(move_event_trigger).to_metta()}\n"
            f'            "No way to go there"\n'
            f"        )\n"
            f"    )\n"
            f")"
        )
