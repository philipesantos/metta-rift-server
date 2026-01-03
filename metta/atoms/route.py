class Route:
    def __init__(self, location_from: str, direction: str, location_to: str):
        self.location_from = location_from
        self.direction = direction
        self.location_to = location_to

    @staticmethod
    def to_metta_usage(location_from: str, direction: str, location_to: str) -> str:
        return f"(Route {location_from} {direction} {location_to})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.location_from, self.direction, self.location_to)}"
