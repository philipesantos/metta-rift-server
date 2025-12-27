from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.route import Route
from metta.events.move_event import MoveEvent
from metta.function import Function
from metta.functions.trigger import Trigger


class MoveTowards(Function):
    def __init__(self, character: Character):
        self.character = character


    @staticmethod
    def to_metta_usage(direction: str) -> str:
        return (
            f"(move-towards {direction})"
        )


    def to_metta_definition(self) -> str:
        current_at_match = CurrentAt.to_metta_usage(self.character.key, "$from")
        route_match = Route.to_meta_usage("$from", "$direction", "$to")
        move_event = MoveEvent("$from", "$to")
        return (
            f"(= (move-towards ($direction))\n"
            f"    (match &self {current_at_match}\n"
            f"        (case (match &self {route_match} $to)\n"
            f"        (\n"
            f'            (Empty "No way to go there")\n'
            f"            ($to {Trigger.to_metta_usage(move_event)})\n"
            f"        ))\n"
            f"    )\n"
            f")"
        )
