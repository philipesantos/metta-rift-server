from metta.events.move_event import MoveEvent
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_describe_location import OnMoveDescribeLocation


class Location:
    def __init__(self, key: str, desc: str):
        self.key = f"lc_{key}"
        self.desc = desc


    @staticmethod
    def to_metta_usage(key: str) -> str:
        return f"(Location {key})"


    def to_metta_definition(self) -> str:
        trigger = Trigger(
            MoveEvent("$from", self.key),
            [
                OnMoveDescribeLocation(self.desc)
            ]
        )
        return (
            f"(: {self.key} Location)\n"
            f"{self.to_metta_usage(self.key)}\n"
            f"{trigger.to_metta_definition()}"
        )
