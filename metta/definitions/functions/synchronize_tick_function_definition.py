from metta.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from metta.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.functions.exists_function_definition import ExistsFunctionDefinition


class SynchronizeTickFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        stale_tick = StaleWrapperPattern("Tick")
        tick_state_match = StateWrapperPattern(TickFactPattern("$tick"))
        tick_state_remove = StateWrapperPattern(TickFactPattern("$current_tick"))
        tick_state_add = StateWrapperPattern(TickFactPattern("$new_tick"))
        return (
            f"(= (synchronize-tick)\n"
            f"    (if {ExistsFunctionPattern(stale_tick).to_metta()}\n"
            f"        (let* (($current_tick (match &self {tick_state_match.to_metta()} $tick))\n"
            f"            ( ()  (remove-atom &self {tick_state_remove.to_metta()}))\n"
            f"            ( ()  (let $new_tick (+ 1 $current_tick) (add-atom &self {tick_state_add.to_metta()})))\n"
            f"            ( ()  (remove-atom &self {stale_tick.to_metta()})))\n"
            f"            Empty\n"
            f"        )\n"
            f"        Empty\n"
            f"    )\n"
            f")"
        )
