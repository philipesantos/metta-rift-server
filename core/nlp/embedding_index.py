from dataclasses import dataclass

import numpy as np
from sentence_transformers import SentenceTransformer

from core.nlp.command_catalog import CommandEntry


@dataclass(frozen=True)
class MatchResult:
    entry: CommandEntry
    score: float


class EmbeddingIndex:
    def __init__(self, entries: list[CommandEntry], model_name: str):
        self.entries = entries
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.embeddings = self._build_embeddings(entries)

    def _build_embeddings(self, entries: list[CommandEntry]) -> np.ndarray:
        if not entries:
            return np.empty((0, 0), dtype=np.float32)
        texts = [entry.utterance for entry in entries]
        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

    def match(self, query: str) -> MatchResult | None:
        if not self.entries:
            return None
        query_vec = self.model.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )[0]
        scores = self.embeddings @ query_vec
        best_idx = int(np.argmax(scores))
        return MatchResult(entry=self.entries[best_idx], score=float(scores[best_idx]))
