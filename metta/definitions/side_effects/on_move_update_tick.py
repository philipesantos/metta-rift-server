from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from metta.definitions.side_effect_definition import SideEffectDefinition


class OnMoveUpdateTick(SideEffectDefinition):
    def to_metta(self) -> str:
        stale_tick = StaleWrapperPattern("Tick")
        return (
            f"(if (exists {stale_tick.to_metta()})\n"
            f"    Empty\n"
            f"    (add-atom &self {stale_tick.to_metta()})\n"
            f")\n"
        )
