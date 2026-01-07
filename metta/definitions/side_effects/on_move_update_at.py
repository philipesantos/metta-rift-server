from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.definitions.side_effect_definition import SideEffectDefinition


class OnMoveUpdateAt(SideEffectDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self, event: MoveEventPattern) -> str:
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        log_move_add_atom = LogWrapperPattern(
            "$current_tick", MoveEventPattern(event.from_location, event.to_location)
        )
        current_at_remove_atom = CurrentAtFactPattern(
            self.character.key, event.from_location
        )
        current_at_add_atom = CurrentAtFactPattern(
            self.character.key, event.to_location
        )
        return (
            f"(let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"    ( ()  (add-atom &self {log_move_add_atom.to_metta()}))\n"
            f"    ( ()  (remove-atom &self {current_at_remove_atom.to_metta()}))\n"
            f"    ( ()  (add-atom &self {current_at_add_atom.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
