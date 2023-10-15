import re
from functools import cache
import itertools
import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt


# don't cache because each number is unique
def make_g_n(num: int) -> nx.DiGraph:
    G = nx.DiGraph()
    if num == 0:
        G.add_node("g0", root=True)
    else:
        for i in range(num):
            G.add_node(f"g{i}", root=True)
            G.add_node(f"v{i+1}")
            G.add_edge(f"g{i}", f"g{i+1}")
            G.add_edge(f"v{i+1}", f"g{i+1}")
    return G


def get_peak(g: nx.DiGraph) -> str:
    # g is a dag tree like so: g0, g0,v1->g1, g1,v2->g2, ...

    g_nodes = [node for node in g.nodes if re.search(r"[A-Za-z]*g\d", node)]
    g_numbers = [int(re.search(r"\d+$", node).group()) for node in g_nodes]
    max_index = g_numbers.index(max(g_numbers))
    return g_nodes[max_index]


ALL_NUMBERS = [make_g_n(i) for i in range(10)]


def determine_number(G: nx.DiGraph) -> int:
    # look for the first isomorphic graph
    for i, num in enumerate(ALL_NUMBERS):
        GM = isomorphism.DiGraphMatcher(G, num)
        if GM.is_isomorphic():
            return i


def combine_graphs(gs: list[nx.DiGraph] | dict[str, nx.DiGraph]) -> nx.DiGraph:
    g_combined = nx.DiGraph()

    if isinstance(gs, dict):
        for prefix, g in gs.items():
            g_combined.add_nodes_from(
                {f"{prefix}/{node}": data for node, data in g.nodes(data=True)}
            )
            g_combined.add_edges_from(
                [(f"{prefix}/{u}", f"{prefix}/{v}") for u, v in g.edges()]
            )
    else:
        for g in gs:
            g_combined.add_nodes_from(g.nodes)
            g_combined.add_edges_from(g.edges)

    return g_combined


def add(gx, gy) -> nx.DiGraph:
    state_graph = combine_graphs({"x": gx, "y": gy})

    uppermost_node_gx = f"x/{get_peak(gx)}"
    lowermost_node_gy = f"y/g0"
    state_graph = nx.relabel_nodes(state_graph, {lowermost_node_gy: uppermost_node_gx})

    return state_graph


def print_graphs(graphs):
    fig, axs = plt.subplots(
        1, len(graphs), figsize=(15, 10)
    )  # Increase the window size
    for i, G in enumerate(graphs):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, ax=axs[i])
    plt.show()


def test_add(x, y):
    gx = make_g_n(x)
    gy = make_g_n(y)
    g_add = add(gx, gy)
    result = determine_number(g_add)
    print(f"{x}+{y}: expected: {x+y}, got: {result}")
    # print_graphs([gx, gy, g_add])


for x, y in itertools.product(range(0, 6), range(4)):
    test_add(x, y)

"""
special nodes:
- chain trees are interpretted as a unary literal
- the times node is a special
- add nodes are for composiing the 1's, 10's, and 100's places

G_145 = <V_145, E_145>
V_145 = { g_{100*1}, g_{10*4}, g_{1*5} } + g_145
E_compo,145 = {
    (g_{100*1}, g_145),
    (g_{10*4}, g_145),
    (g_{1*5}, g_145),
}
E_struct,145 = {
    (g_{100*1}, g_{10*4}),
    (g_{10*4}, g_{1*5}),
}
E_repl,145 = {
    (g_{100*1}, g_{100*1}),
    (g_{10*4}, g_{10*4}),
    (g_{1*5}, g_{1*5}),
}

G_{100*1} = <V_{100*1}, E_{100*1}>
V_{100*1} = { g_{100} } + g_{100*1}

---

v_plus



G = structure | composition | operation
structure = <V, E_s>
composition = <V, E_c>
operation = <V, E_repl>

- replacement edges
- composition edges
- structural edges



"""
