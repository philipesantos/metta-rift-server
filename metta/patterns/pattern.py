from abc import ABC, abstractmethod


class Pattern(ABC):
    @abstractmethod
    def to_metta(self) -> str:
        pass
