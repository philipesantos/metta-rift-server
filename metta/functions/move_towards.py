from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.route import Route
from metta.functions.current import Current
from metta.functions.current_tick import CurrentTick
from metta.functions.exists import Exists
from metta.functions.function import Function


class MoveTowards(Function):
    def __init__(self, character: Character):
        self.character = character


    @staticmethod
    def to_metta_usage(direction: str) -> str:
        return (
            f"(move-towards (${direction}))"
        )


    def to_metta_definition(self) -> str:

        return (
            f"(= (move-towards ($direction))\n"
            f"    (let $current-at (current ((At $tick ch_player $from)))\n"
            f"        (let $from (index-atom $current-at 3)\n"
            f"            (if (exists (Route $from $direction $to))\n"
            f"                (add-atom &self\n"
            f"                    (At (current-tick) ch_player\n"
            f"                        (match &self (Route $from $direction $to) $to)\n"
            f"                    )\n"
            f"                )\n"
            f'                "No way to go there"\n'
            f"            )\n"
            f"        )\n"
            f"    )\n"
            f")"
        )
