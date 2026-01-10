import unittest

from metta.patterns.functions.first_function_pattern import FirstFunctionPattern


class TestFirstFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        value = "(Cons a (Nil))"
        first = FirstFunctionPattern(value)
        self.assertEqual(first.to_metta(), f"(first {value})")


if __name__ == "__main__":
    unittest.main()
