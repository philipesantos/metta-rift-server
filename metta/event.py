from abc import ABC, abstractmethod

class Event(ABC):

    @abstractmethod
    def to_metta(self) -> str:
        pass