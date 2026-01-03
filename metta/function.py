from abc import ABC, abstractmethod


class Function(ABC):
    @abstractmethod
    def to_metta_usage(self, *args) -> str:
        pass

    @abstractmethod
    def to_metta_definition(self) -> str:
        pass
