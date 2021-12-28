# 미로 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
visited[0][0] = True
dist[0][0] = 1
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and map[nx][ny] == '1':
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True

print(dist[n - 1][m - 1])
