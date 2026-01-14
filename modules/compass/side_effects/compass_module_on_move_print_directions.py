from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from modules.compass.patterns.compass_directions_function_pattern import (
    CompassDirectionsFunctionPattern,
)


class CompassModuleOnMovePrintDirections(SideEffectDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self, event: MoveEventPattern) -> str:
        state_at_compass = StateWrapperPattern(AtFactPattern("compass", self.character.key))
        directions = CompassDirectionsFunctionPattern("$to")
        # fmt: off
        return (
            f"(if {ExistsFunctionPattern(state_at_compass).to_metta()}\n"
            f"    {directions.to_metta()}\n"
            f"    Empty\n"
            f")"
        )
        # fmt: on
