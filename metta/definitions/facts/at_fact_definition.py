from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.at_fact_pattern import AtFactPattern


class AtFactDefinition(FactDefinition):
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    def to_metta(self) -> str:
        # fmt: off
        return f"{AtFactPattern(self.what, self.where).to_metta()}"
        # fmt: on
