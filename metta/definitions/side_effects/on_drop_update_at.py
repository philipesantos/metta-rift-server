from metta.definitions.side_effect_definition import SideEffectDefinition
from metta.patterns.events.drop_event_pattern import DropEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class OnDropUpdateAt(SideEffectDefinition):
    def to_metta(self, event: DropEventPattern) -> str:
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        log_drop_add_atom = LogWrapperPattern(
            "$current_tick", DropEventPattern(event.what, event.where)
        )
        state_at_remove_atom = StateWrapperPattern(AtFactPattern(event.what, "player"))
        state_at_add_atom = StateWrapperPattern(AtFactPattern(event.what, event.where))
        return (
            f"(let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"    ( ()  (add-atom &self {log_drop_add_atom.to_metta()}))\n"
            f"    ( ()  (remove-atom &self {state_at_remove_atom.to_metta()}))\n"
            f"    ( ()  (add-atom &self {state_at_add_atom.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
