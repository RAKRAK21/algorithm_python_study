# python 이용할 땐 recursion limit이 1000이라 반드시 sys.setrecursionlimit() 설정해줘야 함. 안그러면 런타임에러
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]

def DFS(graph, v, visited):
    visited[v] = True
        
    for connection in graph[v]:
        if not visited[connection]:
            DFS(graph, connection, visited)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
result = 0
for i in range(1, N+1):
    if not visited[i]:
        DFS(graph, i, visited)
        result += 1

print(result)
