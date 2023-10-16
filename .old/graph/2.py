from __future__ import annotations
import re
from functools import cache, cached_property
import itertools
import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
from typing import Generic, TypeVar
from attrs import attr

T = TypeVar("T")


class Edge(Generic[T], tuple[T, T]):
    pass


@attr.s(auto_attribs=True)
class Symbol:
    atoms: set[Symbol]
    structural_edges: set[Edge[Symbol]]

    replacement: Symbol | None = None

    @cached_property
    def compositional_edges(self) -> set[Edge[Symbol]]:
        return [(atom, self) for atom in self.atoms]

    def __init__(self):
        replacement = replacement or self


class AtomicSymbol(Symbol):
    val: str

    atoms = set()
    structural_edges = set()


# FIXME: in the future there will be a way to instantiate arbitrary numbers
# don't cache because each number is unique
def make_g_n(n: int) -> nx.DiGraph:
    g_n = nx.DiGraph()
    if n == 0:
        g_n.add_node("g0", root=True)
    else:
        for i in range(n):
            g_n.add_node(f"g{i}", root=True)
            g_n.add_node(f"v{i+1}")
            g_n.add_edge(f"g{i}", f"g{i+1}")
            g_n.add_edge(f"v{i+1}", f"g{i+1}")
    return g_n


# NOTE: get a decent representation for doing multi-digit numbers
# NOTE: maybe explore tasks that would teach it new procedures/replacements


# o0 -> o1 -> o2 -> o3
# o0* <-o1' <-o2' <-o'3
