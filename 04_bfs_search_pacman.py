# 4. BFS Search for Pac-Man

from collections import deque

maze = ["P..#", ".#..", "...E"]
start = (0, 0)

q = deque([(start, [start])])
visited = {start}

while q:
    (r, c), path = q.popleft()
    if maze[r][c] == 'E':
        print("Path:", path)
        break
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r+dr, c+dc
        if (0 <= nr < 3 and 0 <= nc < 4
            and maze[nr][nc] != '#'
            and (nr,nc) not in visited):
            visited.add((nr,nc))
            q.append(((nr,nc), path+[(nr,nc)]))
