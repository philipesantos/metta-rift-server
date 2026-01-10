import unittest

from tests.utils.metta import get_test_metta

from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from utils.type import Type
from tests.utils.utils import unwrap_first_match


class TestCharacterFactPattern(unittest.TestCase):
    def test_to_metta(self):
        key = "player"
        name = "John Doe"
        character = CharacterFactPattern(key, name)
        self.assertEqual(
            character.to_metta(), f'({Type.CHARACTER.value} {key} "{name}")'
        )


if __name__ == "__main__":
    unittest.main()
