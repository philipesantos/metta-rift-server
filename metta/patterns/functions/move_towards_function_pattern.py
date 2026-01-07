from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.patterns.function_pattern import FunctionPattern
from utils.direction import Direction


class MoveTowardsFunctionPattern(FunctionPattern):
    def __init__(self, direction: Direction):
        self.direction = direction

    def to_metta(self) -> str:
        return f"(move-towards ({self.direction.value}))"
