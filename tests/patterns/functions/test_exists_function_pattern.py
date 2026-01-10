import unittest

from core.patterns.facts.tick_fact_pattern import TickFactPattern
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from tests.utils.metta import get_test_metta

from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match


class TestExistsFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        pattern = TickFactPattern("0")
        exists = ExistsFunctionPattern(pattern)
        self.assertEqual(exists.to_metta(), f"(exists {pattern.to_metta()})")


if __name__ == "__main__":
    unittest.main()
