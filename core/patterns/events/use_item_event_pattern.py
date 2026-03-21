from core.patterns.event_pattern import EventPattern


class UseItemEventPattern(EventPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self) -> str:
        # fmt: off
        return f"(Use {self.what})"
        # fmt: on
