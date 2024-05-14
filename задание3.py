import matplotlib.pyplot as plt
import networkx as nx

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 3, 'B': 2}
}


G = nx.DiGraph()

G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "A", weight=3)
G.add_edge("C", "B", weight=2)
G.add_edge("B", "A", weight=1)
G.add_edge("B", "C", weight=1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) in path2]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) not in path2]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=300)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()