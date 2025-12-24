from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.route import Route
from metta.functions.current import Current
from metta.functions.current_tick import CurrentTick
from metta.functions.exists import Exists
from metta.functions.function import Function


class MoveTo(Function):
    def __init__(self, character: Character):
        self.character = character


    @staticmethod
    def to_metta_usage(where: str) -> str:
        return (
            f"(move-to (${where}))"
        )


    def to_metta_definition(self) -> str:
        at_current_metta = At.to_metta_usage("$tick", self.character.key, "$from")
        route_exists_metta = Route.to_meta_usage("$from", "$direction", "$to")
        at_exists_metta = At.to_metta_usage("$tick", "$character", "$to")
        current_tick_metta = CurrentTick.to_metta_usage()
        at_add_atom_metta = At.to_metta_usage(current_tick_metta, self.character.key, "$to")
        return (
            f"(= (move-to ($to))\n"
            f"    (let $current-at ${Current.to_metta_usage(at_current_metta)}\n"
            f"        (let $from (index-atom $current-at 3)\n"
            f"            (if\n"
            f"                (and\n"
            f"                    ${Exists.to_metta_usage(route_exists_metta)}\n"
            f"                    ${Exists.to_metta_usage(at_exists_metta)}\n"
            f"                )\n"
            f"                (add-atom &self ${at_add_atom_metta})\n"
            f'                "No way to go there"\n'
            f"            )\n"
            f"        )\n"
            f"    )\n"
            f")"
        )
