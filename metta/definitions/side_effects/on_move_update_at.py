from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.definitions.side_effect_definition import SideEffectDefinition


class OnMoveUpdateAt(SideEffectDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        at_add_atom = AtFactPattern("$current_tick", self.character.key, "$to")
        current_at_remove_atom = CurrentAtFactPattern(self.character.key, "$from")
        current_at_add_atom = CurrentAtFactPattern(self.character.key, "$to")
        return (
            f"(let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"    ( ()  (add-atom &self {at_add_atom.to_metta()}))\n"
            f"    ( ()  (remove-atom &self {current_at_remove_atom.to_metta()}))\n"
            f"    ( ()  (add-atom &self {current_at_add_atom.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
