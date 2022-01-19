# 바이러스
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {k: [] for k in range(1, n + 1)}

def bfs():
    q = deque([1])
    while q:
        node = q.popleft()
        visited[node] = 1
        q.extend([n for n in graph[node] if not visited[n]])

for _ in range(int(input())):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
visited = [0 for _ in range(n + 1)]

bfs()
print(sum(visited) - 1)