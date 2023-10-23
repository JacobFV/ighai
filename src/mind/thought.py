from __future__ import annotations

import numpy as np
from functools import singledispatchmethod
from ighai.utils.similarity import cosine_similarity


class Thought:
    content: str
    embedding: np.ndarray

    emb_sim_fn = cosine_similarity

    def sim(self, other: "Thought") -> float:
        return self.emb_sim_fn(self.embedding, other.embedding)


class CompositeThought(Thought):
    thoughts: list[Thought]
    thought_structure: list[np.ndarray]

    @property
    def embedding(self) -> np.ndarray:
        return np.mean([t.embedding for t in self.thoughts], axis=0)

    @singledispatchmethod
    def sim(self, other: "Thought") -> float:
        return self.emb_sim_fn(self.embedding, other.embedding)

    @sim.register
    def _(self, other: CompositeThought) -> float:
        return np.mean([self.sim(t) for t in other.thoughts])
