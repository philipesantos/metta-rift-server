from core.patterns.event_pattern import EventPattern


class UseEventPattern(EventPattern):
    def __init__(self, what: str, with_what: str):
        self.what = what
        self.with_what = with_what

    def to_metta(self) -> str:
        # fmt: off
        return f"(Use {self.what} {self.with_what})"
        # fmt: on
