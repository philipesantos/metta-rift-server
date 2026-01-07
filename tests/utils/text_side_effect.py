from metta.definitions.side_effect_definition import SideEffectDefinition


class TextSideEffectDefinition(SideEffectDefinition):
    def __init__(self, text: str):
        self.text = text

    def to_metta(self) -> str:
        return f'"{self.text}"'
