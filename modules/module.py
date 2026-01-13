from abc import ABC, abstractmethod

from core.world import World


class Module(ABC):
    @abstractmethod
    def apply(self, world: World) -> None:
        pass
