from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.functions.exists_function_definition import ExistsFunctionDefinition
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern


class MoveToFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        current_at_match = CurrentAtFactPattern(self.character.key, "$from")
        at_exists = AtFactPattern("$tick", self.character.key, "$to")
        move_event = MoveEventPattern("$from", "$to")
        return (
            f"(= (move-to ($to))\n"
            f"    (match &self {current_at_match.to_metta()}\n"
            f"        (if {ExistsFunctionPattern(at_exists).to_metta()}\n"
            f"            {TriggerFunctionPattern(move_event).to_metta()}\n"
            f'            "No way to go there"\n'
            f"        )\n"
            f"    )\n"
            f")"
        )
