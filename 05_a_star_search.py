# 5. A* Search Algorithm

import heapq

graph = {'A': [('B', 1), ('C', 4)],
         'B': [('D', 2)], 'C': [('D', 1)],
         'D': []}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

q = [(h['A'], 0, 'A', ['A'])]

while q:
    f, cost, node, path = heapq.heappop(q)
    if node == 'D':
        print("Path:", path, "Cost:", cost)
        break
    for nxt, w in graph[node]:
        g = cost + w
        heapq.heappush(q, (g+h[nxt], g, nxt, path+[nxt]))
