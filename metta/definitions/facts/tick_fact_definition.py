from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.tick_fact_pattern import TickFactPattern


class TickFactDefinition(FactDefinition):
    def __init__(self, tick: str):
        self.tick = tick

    def to_metta(self) -> str:
        return f"{TickFactPattern(self.tick).to_metta()}"
