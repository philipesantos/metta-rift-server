import unittest

from metta.patterns.functions.move_to_function_pattern import MoveToFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from metta.definitions.functions.move_to_function_definition import (
    MoveToFunctionDefinition,
)
from metta.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from tests.utils.on_move_do_nothing import OnMoveDoNothing
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMoveToFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        where = "glade"
        move_to = MoveToFunctionPattern(where)
        self.assertEqual(move_to.to_metta(), f"(move-to ({where}))")


if __name__ == "__main__":
    unittest.main()
