from core.patterns.fact_pattern import FactPattern
from utils.type import Type


class RouteBlockFactPattern(FactPattern):
    def __init__(self, location_from: str, location_to: str, reason: str):
        self.location_from = location_from
        self.location_to = location_to
        self.reason = reason

    def to_metta(self) -> str:
        reason = self._format_reason()
        # fmt: off
        return (
            f"({Type.ROUTE_BLOCK.value} {self.location_from} "
            f"{self.location_to} {reason})"
        )
        # fmt: on

    def _format_reason(self) -> str:
        if self.reason.startswith("$"):
            return self.reason
        if self.reason.startswith('"') and self.reason.endswith('"'):
            return self.reason
        return f'"{self.reason}"'
