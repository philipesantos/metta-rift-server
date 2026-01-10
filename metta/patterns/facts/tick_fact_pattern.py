from metta.patterns.fact_pattern import FactPattern


class TickFactPattern(FactPattern):
    def __init__(self, tick: str):
        self.tick = tick

    def to_metta(self):
        # fmt: off
        return f"(Tick {self.tick})"
        # fmt: on
