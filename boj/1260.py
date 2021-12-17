# DFS와 BFS

# 정점의 개수 n
# 간선의 개수 m
# 탐색을 시작할 정점의 번호 v

from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    # 노드 연결하기
    graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(start_v):
    discoverd = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)



# 깊이 우선 탐색
def dfs(start_v, discoverd=[]):
    discoverd.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discoverd):
            dfs(w, discoverd)



dfs(v)
print()
bfs(v)
