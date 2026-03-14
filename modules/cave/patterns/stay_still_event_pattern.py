from core.patterns.event_pattern import EventPattern


class StayStillEventPattern(EventPattern):
    def __init__(self, where: str):
        self.where = where

    def to_metta(self) -> str:
        # fmt: off
        return f"(StayStill {self.where})"
        # fmt: on
