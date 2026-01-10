from core.patterns.events.move_event_pattern import MoveEventPattern
from core.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from core.definitions.side_effect_definition import SideEffectDefinition


class OnMoveUpdateTick(SideEffectDefinition):
    def to_metta(self, event: MoveEventPattern) -> str:
        stale_tick = StaleWrapperPattern("Tick")
        # fmt: off
        return (
            f"(if (exists {stale_tick.to_metta()})\n"
            f"    Empty\n"
            f"    (add-atom &self {stale_tick.to_metta()})\n"
            f")\n"
        )
        # fmt: on
