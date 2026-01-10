import unittest

from core.definitions.functions.first_function_definition import (
    FirstFunctionDefinition,
)
from core.patterns.functions.first_function_pattern import FirstFunctionPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestFirstFunctionDefinition(unittest.TestCase):
    def test_first(self):
        metta = get_test_metta()

        metta.run(FirstFunctionDefinition().to_metta())

        list_value = "(Cons apple (Cons sword (Nil)))"
        first = FirstFunctionPattern(list_value)
        result_first = metta.run(f"!{first.to_metta()}")
        self.assertEqual(unwrap_first_match(result_first), "apple")


if __name__ == "__main__":
    unittest.main()
