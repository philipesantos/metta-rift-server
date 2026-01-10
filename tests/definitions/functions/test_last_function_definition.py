import unittest

from core.definitions.functions.last_function_definition import (
    LastFunctionDefinition,
)
from core.patterns.functions.last_function_pattern import LastFunctionPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestLastFunctionDefinition(unittest.TestCase):
    def test_last_singleton(self):
        metta = get_test_metta()

        metta.run(LastFunctionDefinition().to_metta())

        list_value = "(Cons apple (Nil))"
        last = LastFunctionPattern(list_value)
        result_last = metta.run(f"!{last.to_metta()}")
        self.assertEqual(unwrap_first_match(result_last), "apple")

    def test_last_recursive(self):
        metta = get_test_metta()

        metta.run(LastFunctionDefinition().to_metta())

        list_value = "(Cons apple (Cons sword (Cons coin (Nil))))"
        last = LastFunctionPattern(list_value)
        result_last = metta.run(f"!{last.to_metta()}")
        self.assertEqual(unwrap_first_match(result_last), "coin")


if __name__ == "__main__":
    unittest.main()
