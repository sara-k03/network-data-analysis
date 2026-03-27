import numpy as np
import networkx as nx
import pandas as pd
from networkx.algorithms.cluster import all_triangles

adj = pd.read_csv("adjacency_matrices/PC0204N6_216_3D-box_Z3_V_URLa_adj_0.csv", header=None).values
G = nx.from_numpy_array(adj)

triangles = list(nx.all_triangles(G))
print(f"Number of triangles: {len(triangles)}")