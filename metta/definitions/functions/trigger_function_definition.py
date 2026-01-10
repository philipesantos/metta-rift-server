from metta.patterns.event_pattern import EventPattern
from metta.definitions.function_definition import FunctionDefinition
from metta.definitions.side_effect_definition import SideEffectDefinition


class TriggerFunctionDefinition(FunctionDefinition):
    def __init__(self, event: EventPattern, side_effects: list[SideEffectDefinition]):
        self.event = event
        self.side_effects = side_effects

    def to_metta(self) -> str:
        def indent_block(text: str, indent: str = "    ") -> str:
            return "\n".join(
                (indent + line) if line else line for line in text.splitlines()
            )

        # fmt: off
        return "\n".join(
            (
                f"(= (trigger {self.event.to_metta()})\n"
                f"{indent_block(side_effect.to_metta(self.event))}\n"
                f")"
            )
            for side_effect in self.side_effects
        )
        # fmt: on
