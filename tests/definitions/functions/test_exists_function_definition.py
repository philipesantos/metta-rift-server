import unittest

from metta.definitions.facts.at_fact_definition import AtFactDefinition
from metta.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match


class TestExistsFunctionDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())

        at_1 = AtFactDefinition("0", "player", "glade")
        metta.run(at_1.to_metta())

        at_2 = AtFactDefinition("1", "player", "cave")
        metta.run(at_2.to_metta())

        exists_at_1 = ExistsFunctionPattern(
            AtFactPattern(at_1.tick, at_1.what, at_1.where)
        )
        result_exists_at_1 = metta.run(f"!{exists_at_1.to_metta()}")
        self.assertEqual(unwrap_first_match(result_exists_at_1), True)

        exists_at_2 = ExistsFunctionPattern(
            AtFactPattern(at_2.tick, at_2.what, at_2.where)
        )
        result_exists_at_2 = metta.run(f"!{exists_at_2.to_metta()}")
        self.assertEqual(unwrap_first_match(result_exists_at_2), True)

        exists_not_exists = ExistsFunctionPattern(AtFactPattern("1", "player", "beach"))
        result_not_exists = metta.run(f"!{exists_not_exists.to_metta()}")
        self.assertEqual(unwrap_first_match(result_not_exists), False)


if __name__ == "__main__":
    unittest.main()
