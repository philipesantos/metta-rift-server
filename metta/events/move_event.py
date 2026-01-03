from metta.event import Event


class MoveEvent(Event):
    def __init__(self, from_location: str, to_location: str):
        self.from_location = from_location
        self.to_location = to_location

    def to_metta(self) -> str:
        return f"(move {self.from_location} {self.to_location})"
