import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.route import Route
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.move_to import MoveTo
from metta.functions.trigger import Trigger
from tests.utils.on_move_do_nothing import OnMoveDoNothing
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMettaFunctionMoveTo(unittest.TestCase):

    def test_to_metta_usage(self):
        where = "glade"
        move_to_metta_usage = MoveTo.to_metta_usage(where)
        self.assertEqual(move_to_metta_usage, f"(move-to ({where}))")


    def test_to_metta_definition(self):
        metta = get_test_metta()

        character = Character("player", "John")

        metta.run(Exists().to_metta_definition())
        metta.run(MoveTo(character).to_metta_definition())
        metta.run(Trigger(
                MoveEvent("$from", "$to"),
                [OnMoveDoNothing()]
            )
            .to_metta_definition()
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

        move_to_metta_usage_cave = MoveTo.to_metta_usage("cave")
        result_move_to_cave = metta.run(f"!{move_to_metta_usage_cave}")
        self.assertEqual(result_move_to_cave, [[]])

        move_to_metta_usage_plane = MoveTo.to_metta_usage("plane")
        result_move_to_plane = metta.run(f"!{move_to_metta_usage_plane}")
        self.assertEqual(unwrap_first_match(result_move_to_plane), "No way to go there")


if __name__ == "__main__":
    unittest.main()
