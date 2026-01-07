from metta.patterns.fact_pattern import FactPattern


class RouteFactPattern(FactPattern):
    def __init__(self, location_from: str, direction: str, location_to: str):
        self.location_from = location_from
        self.direction = direction
        self.location_to = location_to

    def to_metta(self) -> str:
        return f"(Route {self.location_from} {self.direction} {self.location_to})"
