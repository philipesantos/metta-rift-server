from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.in_fact_pattern import InFactPattern


class InFactDefinition(FactDefinition):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        return f"{InFactPattern(self.what, self.where).to_metta()}"
