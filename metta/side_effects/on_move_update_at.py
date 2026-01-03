from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.wrappers.state import State
from metta.atoms.tick import Tick
from metta.side_effect import SideEffect


class OnMoveUpdateAt(SideEffect):
    def __init__(self, character: Character):
        self.character = character


    def to_metta_definition(self) -> str:
        tick_state_match = State.to_metta_usage(Tick.to_metta_usage("$tick"))
        at_add_atom = At.to_metta_usage("$current_tick", self.character.key, "$to")
        current_at_remove_atom = CurrentAt.to_metta_usage(self.character.key, "$from")
        current_at_add_atom = CurrentAt.to_metta_usage(self.character.key, "$to")
        return (
            f"(let* (($current_tick (match &self {tick_state_match} $tick))\n"
            f"    ( ()  (add-atom &self {at_add_atom}))\n"
            f"    ( ()  (remove-atom &self {current_at_remove_atom}))\n"
            f"    ( ()  (add-atom &self {current_at_add_atom})))\n"
            f'    Empty\n'
            f")\n"
        )
