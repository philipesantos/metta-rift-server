from core.definitions.fact_definition import FactDefinition
from core.patterns.facts.route_block_fact_pattern import RouteBlockFactPattern


class RouteBlockFactDefinition(FactDefinition):
    def __init__(self, location_from: str, location_to: str, reason: str):
        self.location_from = location_from
        self.location_to = location_to
        self.reason = reason

    def to_metta(self) -> str:
        # fmt: off
        return (
            f"{RouteBlockFactPattern(self.location_from, self.location_to, self.reason).to_metta()}"
        )
        # fmt: on
