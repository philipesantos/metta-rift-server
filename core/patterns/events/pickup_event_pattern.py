from core.patterns.event_pattern import EventPattern


class PickUpEventPattern(EventPattern):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        # fmt: off
        return f"(PickUp {self.what} {self.where})"
        # fmt: on
