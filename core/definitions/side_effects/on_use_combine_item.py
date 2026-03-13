from typing import Union

from core.definitions.facts.container_fact_definition import ContainerFactDefinition
from core.definitions.facts.item_fact_definition import ItemFactDefinition
from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class OnUseCombineItem(SideEffectDefinition):
    def __init__(
        self,
        target_item: Union[ItemFactDefinition, ContainerFactDefinition],
        used_item: ItemFactDefinition,
        new_item: Union[ItemFactDefinition, ContainerFactDefinition],
    ):
        self.target_item = target_item
        self.used_item = used_item
        self.new_item = new_item

    def to_metta(self, event: UseEventPattern) -> str:
        target_item_state = StateWrapperPattern(
            AtFactPattern(self.target_item.key, "$target_item_where")
        )
        used_item_state = StateWrapperPattern(
            AtFactPattern(self.used_item.key, "$used_item_where")
        )
        new_item_state = StateWrapperPattern(
            AtFactPattern(self.new_item.key, "$target_item_where")
        )
        return (
            f"(let* (\n"
            f"    (() (match &self {target_item_state.to_metta()} (remove-atom &self {target_item_state.to_metta()})))\n"
            f"    (() (add-atom &self {new_item_state.to_metta()}))\n"
            f"    (() (match &self {used_item_state.to_metta()} (remove-atom &self {used_item_state.to_metta()})))\n"
            f")\n"
            f"    Empty\n"
            f")\n"
        )
