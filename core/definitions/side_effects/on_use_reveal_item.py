from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.event_pattern import EventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class OnUseRevealItem(SideEffectDefinition):
    def __init__(self, item_key: str, where: str, remove_target_key: str | None = None):
        self.item_key = item_key
        self.where = where
        self.remove_target_key = remove_target_key

    def to_metta(self, event: EventPattern) -> str:
        item_state = StateWrapperPattern(AtFactPattern(self.item_key, self.where))
        if self.remove_target_key is None:
            return (
                f"(let* ((() (add-atom &self {item_state.to_metta()})))\n"
                f"    Empty\n"
                f")\n"
            )

        target_state = StateWrapperPattern(
            AtFactPattern(self.remove_target_key, self.where)
        )
        return (
            f"(let* ((() (add-atom &self {item_state.to_metta()}))\n"
            f"    (() (remove-atom &self {target_state.to_metta()})))\n"
            f"    Empty\n"
            f")\n"
        )
