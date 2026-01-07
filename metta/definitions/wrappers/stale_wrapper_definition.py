from metta.definitions.wrapper_definition import WrapperDefinition
from metta.patterns.wrapper_pattern import WrapperPattern
from metta.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern


class StaleWrapperDefinition(WrapperDefinition):
    def __init__(self, what: str):
        self.what = what

    def to_metta(self):
        return StaleWrapperPattern(self.what).to_metta()
