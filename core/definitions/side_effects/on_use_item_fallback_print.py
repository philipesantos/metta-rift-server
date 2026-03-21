from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.use_item_event_pattern import UseItemEventPattern
from core.patterns.facts.response_fact_pattern import ResponseFactPattern
from core.patterns.facts.supported_single_use_fact_pattern import (
    SupportedSingleUseFactPattern,
)
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern


class OnUseItemFallbackPrint(SideEffectDefinition):
    def __init__(self, text: str = "That doesn't seem to do anything."):
        self.text = text

    def to_metta(self, event: UseItemEventPattern) -> str:
        supported_use = SupportedSingleUseFactPattern(event.what)
        response = ResponseFactPattern(100, f'"{self.text}"').to_metta()
        return (
            f"(if {ExistsFunctionPattern(supported_use).to_metta()}\n"
            f"    Empty\n"
            f"    {response}\n"
            f")"
        )
