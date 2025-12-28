from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.side_effect import SideEffect


class OnMoveDescribeLocation(SideEffect):
    def __init__(self, description: str):
        self.description = description


    def to_metta_definition(self) -> str:
        return (
            f'"{self.description}"'
        )
