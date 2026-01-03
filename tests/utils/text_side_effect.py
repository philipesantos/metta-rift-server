from metta.side_effect import SideEffect


class TextSideEffect(SideEffect):
    def __init__(self, text: str):
        self.text = text

    def to_metta_definition(self) -> str:
        return f'"{self.text}"'
