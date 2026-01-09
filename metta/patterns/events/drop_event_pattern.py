from metta.patterns.event_pattern import EventPattern


class DropEventPattern(EventPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"(Drop {self.what} {self.where})"
