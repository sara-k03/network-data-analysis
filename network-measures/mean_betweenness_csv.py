import numpy as np
import networkx as nx
import pandas as pd

adj = pd.read_csv("adjacency_matrices/PC0204N6_216_3D-box_Z3_V_URLa_adj_0.csv", header=None).values
G = nx.from_numpy_array(adj)

betweenness = nx.betweenness_centrality(G, normalized=True, weight='weight')
mean_betweenness = np.mean(list(betweenness.values()))
print(f"Mean betweenness centrality: {mean_betweenness}")