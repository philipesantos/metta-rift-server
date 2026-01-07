from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.functions.exists_function_definition import ExistsFunctionDefinition
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.patterns.function_pattern import FunctionPattern


class MoveToFunctionPattern(FunctionPattern):
    def __init__(self, where: str):
        self.where = where

    def to_metta(self) -> str:
        return f"(move-to ({self.where}))"
