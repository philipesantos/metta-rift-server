from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.events.move_event import MoveEvent
from metta.function import Function
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger


class MoveTo(Function):
    def __init__(self, character: Character):
        self.character = character

    @staticmethod
    def to_metta_usage(where: str) -> str:
        return f"(move-to ({where}))"

    def to_metta_definition(self) -> str:
        current_at_match = CurrentAt.to_metta_usage(self.character.key, "$from")
        at_exists = At.to_metta_usage("$tick", self.character.key, "$to")
        move_event = MoveEvent("$from", "$to")
        return (
            f"(= (move-to ($to))\n"
            f"    (match &self {current_at_match}\n"
            f"        (if {Exists.to_metta_usage(at_exists)}\n"
            f"            {Trigger.to_metta_usage(move_event)}\n"
            f'            "No way to go there"\n'
            f"        )\n"
            f"    )\n"
            f")"
        )
