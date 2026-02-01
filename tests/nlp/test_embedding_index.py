import unittest

from core.nlp import CommandEntry, EmbeddingIndex


class TestEmbeddingIndex(unittest.TestCase):
    def test_matches_best_entry_for_query(self):
        entries = [
            CommandEntry(
                utterance="pickup compass",
                intent="pickup",
                metta="(pickup (compass))",
                slots={"item": "compass"},
            ),
            CommandEntry(
                utterance="drop compass",
                intent="drop",
                metta="(drop (compass))",
                slots={"item": "compass"},
            ),
        ]

        index = EmbeddingIndex(entries, model_name="BAAI/bge-small-en-v1.5")
        match = index.match("pickup compass")

        self.assertIsNotNone(match)
        self.assertEqual(match.entry.utterance, "pickup compass")


if __name__ == "__main__":
    unittest.main()
