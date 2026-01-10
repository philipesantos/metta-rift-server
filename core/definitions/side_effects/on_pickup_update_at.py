from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.pickup_event_pattern import PickUpEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.facts.tick_fact_pattern import TickFactPattern
from core.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class OnPickUpUpdateAt(SideEffectDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self, event: PickUpEventPattern) -> str:
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        log_pickup_add_atom = LogWrapperPattern(
            "$current_tick", PickUpEventPattern(event.what, event.where)
        )
        state_at_match = StateWrapperPattern(AtFactPattern(event.what, "$where_match"))
        state_at_add_atom = StateWrapperPattern(
            AtFactPattern(event.what, self.character.key)
        )
        # fmt: off
        return (
            f"(let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"    ( ()  (add-atom &self {log_pickup_add_atom.to_metta()}))\n"
            f"    ( ()  (match &self {state_at_match.to_metta()}\n"
            f"        (remove-atom &self {state_at_match.to_metta()})))\n"
            f"    ( ()  (add-atom &self {state_at_add_atom.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
        # fmt: on
