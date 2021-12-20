import math

nodes = int(input("Enter total number of nodes: "))
edges = int(input("Enter total number of edges: "))
costs = [0] * nodes
dest = [0] * nodes # noqa
path = [0] * nodes
cost_matrix = [[0]*nodes for _ in range(nodes)]

for _ in range(edges):
    edg = input("Enter edge start edge end and cost separated by spaces: ").split(" ")
    i, j, c = int(edg[0]), int(edg[1]), int(edg[2])
    cost_matrix[i][j] = c
    cost_matrix[j][i] = c
print(*cost_matrix, sep="\n")

for ni in reversed(range(nodes)):
    min_cost = math.inf
    for nk in range(ni + 1, nodes):
        if cost_matrix[ni][nk] != 0 and ((cost_matrix[ni][nk] + costs[nk]) < min_cost):
            min_cost = cost_matrix[ni][nk] + costs[nk]
            dest[ni] = nk
            costs[ni] = min_cost

print(costs, dest)
path = 0
print(path, end="")
while path != nodes - 1:
    path = dest[path]
    print(" -> "+str(path), end="")
# Sample Cost matrix inp

# Enter total number of nodes: 12
# Enter total number of edges: 21
# Enter edge start edge end and cost separated by spaces: 0 1 9
# Enter edge start edge end and cost separated by spaces: 0 2 7
# Enter edge start edge end and cost separated by spaces: 0 3 3
# Enter edge start edge end and cost separated by spaces: 0 4 2
# Enter edge start edge end and cost separated by spaces: 1 5 4
# Enter edge start edge end and cost separated by spaces: 1 6 2
# Enter edge start edge end and cost separated by spaces: 1 7 1
# Enter edge start edge end and cost separated by spaces: 2 5 2
# Enter edge start edge end and cost separated by spaces: 2 6 7
# Enter edge start edge end and cost separated by spaces: 3 7 11
# Enter edge start edge end and cost separated by spaces: 4 6 11
# Enter edge start edge end and cost separated by spaces: 4 7 8
# Enter edge start edge end and cost separated by spaces: 5 8 6
# Enter edge start edge end and cost separated by spaces: 5 9 5
# Enter edge start edge end and cost separated by spaces: 6 8 4
# Enter edge start edge end and cost separated by spaces: 6 9 3
# Enter edge start edge end and cost separated by spaces: 7 9 5
# Enter edge start edge end and cost separated by spaces: 7 10 6
# Enter edge start edge end and cost separated by spaces: 8 11 4
# Enter edge start edge end and cost separated by spaces: 9 11 2
# Enter edge start edge end and cost separated by spaces: 10 11 5
# [0, 9, 7, 3, 2, 0, 0, 0, 0, 0, 0, 0],
# [9, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0],
# [7, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0],
# [3, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 11, 8, 0, 0, 0, 0],
# [0, 4, 2, 0, 0, 0, 0, 0, 6, 5, 0, 0],
# [0, 2, 7, 0, 11, 0, 0, 0, 4, 3, 0, 0],
# [0, 1, 0, 11, 8, 0, 0, 0, 0, 5, 6, 0],
# [0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 0, 4],
# [0, 0, 0, 0, 0, 5, 3, 5, 0, 0, 0, 2],
# [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5],
# [0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 5, 0]
# [16, 7, 9, 18, 15, 7, 5, 7, 4, 2, 5, 0] [1, 6, 5, 7, 7, 9, 9, 9, 11, 11, 11, 0]
# 0->1->6->9->11
