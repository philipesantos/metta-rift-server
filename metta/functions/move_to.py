from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.route import Route
from metta.events.move_event import MoveEvent
from metta.function import Function
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger


class MoveTo(Function):
    def __init__(self, character: Character):
        self.character = character


    @staticmethod
    def to_metta_usage(where: str) -> str:
        return (
            f"(move-to {where})"
        )


    def to_metta_definition(self) -> str:
        current_at_match = CurrentAt.to_metta_usage(self.character.key, "$from")
        route_exists = Route.to_meta_usage("$from", "$direction", "$to")
        at_exists = At.to_metta_usage("$tick", "$character", "$to")
        move_event = MoveEvent("$from", "$to")
        return (
            f"(= (move-to ($to))\n"
            f"    (match &self {current_at_match}\n"
            f"        (if\n"
            f"            (and\n"
            f"                {Exists.to_metta_usage(route_exists)}\n"
            f"                {Exists.to_metta_usage(at_exists)}\n"
            f"            )\n"
            f"            {Trigger.to_metta_usage(move_event)}\n"
            f'            "No way to go there"\n'
            f"        )\n"
            f"    )\n"
            f")"
        )
