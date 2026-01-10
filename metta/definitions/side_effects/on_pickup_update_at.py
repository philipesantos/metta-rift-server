from metta.definitions.side_effect_definition import SideEffectDefinition
from metta.patterns.events.pickup_event_pattern import PickUpEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class OnPickUpUpdateAt(SideEffectDefinition):
    def to_metta(self, event: PickUpEventPattern) -> str:
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        log_pickup_add_atom = LogWrapperPattern(
            "$current_tick", PickUpEventPattern(event.what, event.where)
        )
        state_at_match = StateWrapperPattern(
            AtFactPattern(event.what, "$where_match")
        )
        state_at_add_atom = StateWrapperPattern(AtFactPattern(event.what, "player"))
        return (
            f"(let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"    ( ()  (add-atom &self {log_pickup_add_atom.to_metta()}))\n"
            f"    ( ()  (match &self {state_at_match.to_metta()} "
            f"        (remove-atom &self {state_at_match.to_metta()})))\n"
            f"    ( ()  (add-atom &self {state_at_add_atom.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
