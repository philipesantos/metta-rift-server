import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.route import Route
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.move_to import MoveTo
from metta.functions.move_towards import MoveTowards
from metta.functions.trigger import Trigger
from tests.utils.on_move_do_nothing import OnMoveDoNothing
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMettaFunctionMoveTowards(unittest.TestCase):
    def test_to_metta_usage(self):
        direction = Direction.WEST.value
        move_towards_metta_usage = MoveTowards.to_metta_usage(direction)
        self.assertEqual(move_towards_metta_usage, f"(move-towards ({direction}))")

    def test_to_metta_definition(self):
        metta = get_test_metta()

        character = Character("player", "John")

        metta.run(MoveTowards(character).to_metta_definition())
        metta.run(
            Trigger(
                MoveEvent("$from", "$to"), [OnMoveDoNothing()]
            ).to_metta_definition()
        )

        metta.run(Route("cave", Direction.NORTH.value, "beach").to_metta_definition())
        metta.run(Route("beach", Direction.NORTH.value, "glade").to_metta_definition())
        metta.run(Route("glade", Direction.SOUTH.value, "beach").to_metta_definition())
        metta.run(Route("beach", Direction.SOUTH.value, "cave").to_metta_definition())
        metta.run(Route("cave", Direction.SOUTH.value, "plane").to_metta_definition())

        metta.run(At("0", character.key, "cave").to_metta_definition())
        metta.run(At("1", character.key, "beach").to_metta_definition())
        metta.run(At("2", character.key, "glade").to_metta_definition())

        current_at = CurrentAt(character.key, "glade")
        metta.run(current_at.to_metta_definition())

        move_towards_metta_usage_west = MoveTowards.to_metta_usage(Direction.WEST.value)
        result_move_towards_west = metta.run(f"!{move_towards_metta_usage_west}")
        self.assertEqual(
            unwrap_first_match(result_move_towards_west), "No way to go there"
        )

        move_towards_metta_usage_south = MoveTowards.to_metta_usage(
            Direction.SOUTH.value
        )
        result_move_towards_south = metta.run(f"!{move_towards_metta_usage_south}")
        self.assertEqual(result_move_towards_south, [[]])


if __name__ == "__main__":
    unittest.main()
