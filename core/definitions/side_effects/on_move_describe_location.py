from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.move_event_pattern import MoveEventPattern


class OnMoveDescribeLocation(SideEffectDefinition):
    def __init__(self, description: str):
        self.description = description

    def to_metta(self, event: MoveEventPattern) -> str:
        # fmt: off
        return f'"{self.description}"'
        # fmt: on
