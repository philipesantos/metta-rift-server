from core.patterns.fact_pattern import FactPattern
from utils.type import Type


class RouteFactPattern(FactPattern):
    def __init__(self, location_from: str, direction: str, location_to: str):
        self.location_from = location_from
        self.direction = direction
        self.location_to = location_to

    def to_metta(self) -> str:
        # fmt: off
        return (
            f"({Type.ROUTE.value} {self.location_from} {self.direction} "
            f"{self.location_to})"
        )
        # fmt: on
