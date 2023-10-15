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


ALL_NUMBERS = [make_g_n(i) for i in range(10)]


def determine_number(G: nx.DiGraph) -> int:
    # look for the first isomorphic graph
    for i, num in enumerate(ALL_NUMBERS):
        GM = isomorphism.DiGraphMatcher(G, num)
        if GM.is_isomorphic():
            return i


# # def evolve(state: nx.DiGraph, operators: list[nx.DiGraph]) -> nx.DiGraph:
# def evolve(state: nx.DiGraph) -> nx.DiGraph:
#     pass


# g_add_operator = nx.DiGraph()
# g_op = g -> g'
# g -> x,y,u,x,,r
# g' -> x,u,r


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

    # the uppermost node of the first addend points to the bottommost node of the 2nd addend
    # assuming the uppermost node of gx is "g0" and the bottommost node of gy is "g{len(gy.nodes)}"
    uppermost_node_gx = f"x/g{len(gx.nodes)}"
    bottommost_node_gy = "y/g0"

    state_graph.add_edge(uppermost_node_gx, bottommost_node_gy)

    return state_graph


# # Find subgraphs that match the pattern
# for sub_nodes in nx.ego_graph(G, "g1"):
#     subgraph = G.subgraph(sub_nodes)
#     GM2 = isomorphism.DiGraphMatcher(subgraph, GM)
#     if GM2.is_isomorphic():
#         print("Found a match!")
#         # Replace the subgraph
#         mapping = {"v2": "v2_replaced"}
#         G = nx.relabel_nodes(G, mapping)


# Function to print the graphs
def print_graphs(graphs):
    fig, axs = plt.subplots(1, len(graphs))
    for i, G in enumerate(graphs):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, ax=axs[i])
    plt.show()


def test_add(x, y):
    gx = make_g_n(x)
    gy = make_g_n(y)
    g_add = add(gx, gy)
    print_graphs([gx, gy, g_add])
    result = determine_number(g_add)
    print(f"{x}+{y}: expected: {x+y}, got: {result}")


for x, y in itertools.product(range(10), range(10)):
    test_add(x, y)
