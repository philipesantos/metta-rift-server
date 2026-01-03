from abc import ABC, abstractmethod


class SideEffect(ABC):
    @abstractmethod
    def to_metta_definition(self) -> str:
        pass
