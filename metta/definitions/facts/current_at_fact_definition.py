from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern


class CurrentAtFactDefinition(FactDefinition):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"{CurrentAtFactPattern(self.what, self.where).to_metta()}"
