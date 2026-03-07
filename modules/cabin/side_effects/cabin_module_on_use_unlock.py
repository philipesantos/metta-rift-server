from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.facts.route_block_fact_pattern import RouteBlockFactPattern


class CabinModuleOnUseUnlock(SideEffectDefinition):
    def __init__(self, location_from: str, location_to: str):
        self.location_from = location_from
        self.location_to = location_to

    def to_metta(self, event: UseEventPattern) -> str:
        route_block_match = RouteBlockFactPattern(
            self.location_from,
            self.location_to,
            "$reason",
        )
        # fmt: off
        return (
            f"(let* ((() (match &self {route_block_match.to_metta()}\n"
            f"    (remove-atom &self {route_block_match.to_metta()}))))\n"
            f"    Empty\n"
            f")\n"
        )
        # fmt: on
