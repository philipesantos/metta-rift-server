from abc import ABC, abstractmethod


class Definition(ABC):
    @abstractmethod
    def to_metta(self) -> str:
        pass
