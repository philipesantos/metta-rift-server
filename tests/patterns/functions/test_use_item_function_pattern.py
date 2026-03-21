import unittest

from core.patterns.functions.use_item_function_pattern import UseItemFunctionPattern


class TestUseItemFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        use_function = UseItemFunctionPattern("lantern")
        self.assertEqual(use_function.to_metta(), "(use (lantern))")


if __name__ == "__main__":
    unittest.main()
