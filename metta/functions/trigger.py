from metta.event import Event
from metta.function import Function
from metta.side_effect import SideEffect


class Trigger(Function):
    def __init__(self, event: Event, side_effects: list[SideEffect]):
        self.event = event
        self.side_effects = side_effects


    @staticmethod
    def to_metta_usage(event: Event) -> str:
        return (
            f"(trigger {event.to_metta()})"
        )

    def to_metta_definition(self) -> str:
        def indent_block(text: str, indent: str = "    ") -> str:
            return "\n".join(
                (indent + line) if line else line
                for line in text.splitlines()
            )

        return "\n".join(
            (
                f"(= (trigger {self.event.to_metta()})\n"
                f"{indent_block(side_effect.to_metta_definition())}\n"
                f")"
            )
            for side_effect in self.side_effects
        )
