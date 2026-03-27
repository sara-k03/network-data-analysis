import numpy as np
import networkx as nx
import pandas as pd

adj = pd.read_csv("adjacency_matrices/PC0204N6_216_3D-box_Z3_V_URLa_adj_0.csv", header=None).values
G = nx.from_numpy_array(adj)

avg_clustering_a0 = nx.average_clustering(G)
print(f"a=0: Average clustering coefficient = {avg_clustering_a0}")