from abc import ABC, abstractmethod

from metta.patterns.event_pattern import EventPattern


class SideEffectDefinition(ABC):
    @abstractmethod
    def to_metta(self, event: EventPattern) -> str:
        pass
