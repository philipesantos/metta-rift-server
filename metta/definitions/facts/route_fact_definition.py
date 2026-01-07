from metta.definitions.fact_definition import FactDefinition
from metta.patterns.facts.route_fact_pattern import RouteFactPattern


class RouteFactDefinition(FactDefinition):
    def __init__(self, location_from: str, direction: str, location_to: str):
        self.location_from = location_from
        self.direction = direction
        self.location_to = location_to

    def to_metta(self) -> str:
        return f"{RouteFactPattern(self.location_from, self.direction, self.location_to).to_metta()}"
