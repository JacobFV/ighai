import networkx as nx
from networkx.algorithms import isomorphism

# Define the first graph
G1 = nx.Graph()
G1.add_edges_from([("v1", "v2"), ("v2", "v3")])

# Define the second graph
G2 = nx.Graph()
G2.add_edges_from([("v1", "v2"), ("v2", "v3"), ("v3", "v1")])

# Create a matcher object
GM = isomorphism.GraphMatcher(G2, G1)

# Find subgraph isomorphisms
for subgraph in GM.subgraph_isomorphisms_iter():
    print(subgraph)
