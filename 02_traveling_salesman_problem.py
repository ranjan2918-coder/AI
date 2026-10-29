# 2. Traveling Salesman Problem (TSP)

from itertools import permutations

d = [[0, 10, 15, 20],
     [10, 0, 35, 25],
     [15, 35, 0, 30],
     [20, 25, 30, 0]]

paths = [(sum(d[p[i]][p[i+1]] for i in range(2)) + d[p[2]][p[0]],
          (0,) + p + (0,))
         for p in permutations([1, 2, 3])]

cost, path = min(paths)
print("Path:", path)
print("Cost:", cost)
