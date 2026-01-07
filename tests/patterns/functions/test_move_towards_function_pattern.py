import unittest

from metta.patterns.functions.move_towards_function_pattern import MoveTowardsFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.move_towards_function_definition import MoveTowardsFunctionDefinition
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from tests.utils.on_move_do_nothing import OnMoveDoNothing
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMoveTowardsFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        direction = Direction.WEST
        move_towards = MoveTowardsFunctionPattern(direction)
        self.assertEqual(move_towards.to_metta(), f"(move-towards ({direction.value}))")


if __name__ == "__main__":
    unittest.main()
