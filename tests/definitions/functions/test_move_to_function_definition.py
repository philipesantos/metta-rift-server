import unittest

from metta.definitions.facts.at_fact_definition import AtFactDefinition
from metta.definitions.facts.current_at_fact_definition import CurrentAtFactDefinition
from metta.definitions.facts.route_fact_definition import RouteFactDefinition
from metta.patterns.functions.move_to_function_pattern import MoveToFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.exists_function_definition import ExistsFunctionDefinition
from metta.definitions.functions.move_to_function_definition import MoveToFunctionDefinition
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from tests.utils.on_move_do_nothing import OnMoveDoNothing
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMoveToFunctionDefinition(unittest.TestCase):

    def test_to_metta(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(MoveToFunctionDefinition(character).to_metta())
        metta.run(
            TriggerFunctionDefinition(
                MoveEventPattern("$from", "$to"), [OnMoveDoNothing()]
            ).to_metta()
        )

        metta.run(RouteFactDefinition("cave", Direction.NORTH.value, "beach").to_metta())
        metta.run(RouteFactDefinition("beach", Direction.NORTH.value, "glade").to_metta())
        metta.run(RouteFactDefinition("glade", Direction.SOUTH.value, "beach").to_metta())
        metta.run(RouteFactDefinition("beach", Direction.SOUTH.value, "cave").to_metta())
        metta.run(RouteFactDefinition("cave", Direction.SOUTH.value, "plane").to_metta())

        metta.run(AtFactDefinition("0", character.key, "cave").to_metta())
        metta.run(AtFactDefinition("1", character.key, "beach").to_metta())
        metta.run(AtFactDefinition("2", character.key, "glade").to_metta())

        current_at = CurrentAtFactDefinition(character.key, "glade")
        metta.run(current_at.to_metta())

        move_to_cave = MoveToFunctionPattern("cave")
        result_move_to_cave = metta.run(f"!{move_to_cave.to_metta()}")
        self.assertEqual(result_move_to_cave, [[]])

        move_to_plane = MoveToFunctionPattern("plane")
        result_move_to_plane = metta.run(f"!{move_to_plane.to_metta()}")
        self.assertEqual(unwrap_first_match(result_move_to_plane), "No way to go there")


if __name__ == "__main__":
    unittest.main()
