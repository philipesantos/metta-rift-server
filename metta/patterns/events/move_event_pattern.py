from metta.patterns.event_pattern import EventPattern


class MoveEventPattern(EventPattern):
    def __init__(self, from_location: str, to_location: str):
        self.from_location = from_location
        self.to_location = to_location

    def to_metta(self) -> str:
        return f"(Move {self.from_location} {self.to_location})"
