from metta.patterns.wrapper_pattern import WrapperPattern


class StaleWrapperPattern(WrapperPattern):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self):
        # fmt: off
        return f"(Stale {self.what})"
        # fmt: on
