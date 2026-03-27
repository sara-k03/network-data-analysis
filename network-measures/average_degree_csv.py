import csv
from collections import Counter

filename = "adjacency_matrices/PC0204N6_216_3D-box_Z3_V_URLa_adj_0.csv"

matrix = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        matrix.append([int(x) for x in row])

n = len(matrix)
degrees = [sum(row) for row in matrix]

avg_degree = sum(degrees) / n
total_edges = sum(degrees) // 2  # divide by 2 for undirected graph

print(f"Number of nodes:          {n}")
print(f"Total edges:              {total_edges}")
print(f"Average degree per node:  {avg_degree:.4f}")