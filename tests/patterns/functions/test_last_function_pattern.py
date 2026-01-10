import unittest

from core.patterns.functions.last_function_pattern import LastFunctionPattern


class TestLastFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        value = "(Cons a (Nil))"
        last = LastFunctionPattern(value)
        self.assertEqual(last.to_metta(), f"(last {value})")


if __name__ == "__main__":
    unittest.main()
