from core.patterns.event_pattern import EventPattern


class StartupEventPattern(EventPattern):
    def to_metta(self) -> str:
        # fmt: off
        return "(Startup)"
        # fmt: on
