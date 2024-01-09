import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
visited[0] = True

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
    return 0
    
for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
    else:
        continue

print(cnt)