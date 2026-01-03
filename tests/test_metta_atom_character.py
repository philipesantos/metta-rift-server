import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.character import Character
from tests.utils.utils import unwrap_first_match


class TestMettaAtomCharacter(unittest.TestCase):
    def test_to_metta_usage(self):
        key = "player"
        name = "John Doe"
        character_metta_usage = Character.to_metta_usage(key, name)
        self.assertEqual(character_metta_usage, f'(Character {key} "{name}")')

    def test_to_metta_definition(self):
        metta = get_test_metta()

        key = "player"
        name = "John"

        character_metta_definition = Character(key, name).to_metta_definition()
        metta.run(character_metta_definition)

        result_type = metta.run(f"!(get-type {key})")
        self.assertEqual(unwrap_first_match(result_type), "Character")

        character_metta_usage_key = Character.to_metta_usage("$key", name)
        result_key = metta.run(f"!(match &self {character_metta_usage_key} $key)")
        self.assertEqual(unwrap_first_match(result_key), key)

        character_metta_usage_name = Character.to_metta_usage(key, "$name")
        result_name = metta.run(f"!(match &self {character_metta_usage_name} $name)")
        self.assertEqual(unwrap_first_match(result_name), name)

        character_metta_usage_no_match = Character.to_metta_usage("james", name)
        result_no_match = metta.run(
            f"!(match &self {character_metta_usage_no_match} True)"
        )
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
