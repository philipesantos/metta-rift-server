from metta.definitions.side_effect_definition import SideEffectDefinition


class OnMoveDescribeLocation(SideEffectDefinition):
    def __init__(self, description: str):
        self.description = description

    def to_metta(self) -> str:
        return f'"{self.description}"'
