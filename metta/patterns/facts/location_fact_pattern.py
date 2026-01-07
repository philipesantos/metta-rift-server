from metta.patterns.fact_pattern import FactPattern


class LocationFactPattern(FactPattern):
    def __init__(self, key: str):
        self.key = f"{key}"

    def to_metta(self) -> str:
        return f"(Location {self.key})"
