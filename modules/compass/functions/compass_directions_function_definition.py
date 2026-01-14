from core.definitions.function_definition import FunctionDefinition
from core.patterns.facts.route_fact_pattern import RouteFactPattern


class CompassDirectionsFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        route = RouteFactPattern("$from", "$direction", "$_")
        # fmt: off
        return (
            f"(= (compass-directions ($from))\n"
            f'    ("You can go: " (collapse (match &self {route.to_metta()} $direction)))\n'
            f")"
        )
        # fmt: on
