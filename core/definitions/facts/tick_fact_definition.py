from core.definitions.fact_definition import FactDefinition
from core.patterns.facts.tick_fact_pattern import TickFactPattern


class TickFactDefinition(FactDefinition):
    def __init__(self, tick: str):
        self.tick = tick

    def to_metta(self) -> str:
        # fmt: off
        return f"{TickFactPattern(self.tick).to_metta()}"
        # fmt: on
