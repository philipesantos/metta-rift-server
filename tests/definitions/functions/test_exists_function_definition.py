import unittest

from core.definitions.facts.at_fact_definition import AtFactDefinition
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from tests.utils.metta import get_test_metta

from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match


class TestExistsFunctionDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())

        at_1 = AtFactDefinition("player", "glade")
        metta.run(at_1.to_metta())

        at_2 = AtFactDefinition("player", "cave")
        metta.run(at_2.to_metta())

        exists_at_1 = ExistsFunctionPattern(AtFactPattern(at_1.what, at_1.where))
        result_exists_at_1 = metta.run(f"!{exists_at_1.to_metta()}")
        self.assertEqual(unwrap_first_match(result_exists_at_1), True)

        exists_at_2 = ExistsFunctionPattern(AtFactPattern(at_2.what, at_2.where))
        result_exists_at_2 = metta.run(f"!{exists_at_2.to_metta()}")
        self.assertEqual(unwrap_first_match(result_exists_at_2), True)

        exists_not_exists = ExistsFunctionPattern(AtFactPattern("player", "beach"))
        result_not_exists = metta.run(f"!{exists_not_exists.to_metta()}")
        self.assertEqual(unwrap_first_match(result_not_exists), False)


if __name__ == "__main__":
    unittest.main()
