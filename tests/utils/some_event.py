from metta.event import Event


class SomeEvent(Event):
    def __init__(self, value: str):
        self.value = value


    def to_metta(self) -> str:
        return f"(some event {self.value})"
