# #1260(DFS, BFS 공부하기)
# import sys
# from collections import deque


# input = sys.stdin.readline
# n, m, v = map(int, input().split())
# graph = [[False] * (n + 1) for _ in range(n + 1)]

# visited_dfs = [False] * (n + 1)
# visited_bfs = [False] * (n + 1)

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = graph[b][a] = 1

# def dfs(v):
#     visited_dfs[v] = True
#     print(v, end = " ")
#     for i in range(1, n+1):
#         if not visited_dfs[i] and graph[v][i] == 1:
#             dfs(i)



# def bfs(v):
#     queue = deque([v])
#     visited_bfs[v] = True

#     while queue:
#         v= queue.popleft()
#         print(v, end = " ")
#         for i in range(1, n+1):
#             if not visited_bfs[i] and graph[v][i] == 1:
#                 queue.append(i)
#                 visited_bfs[i] = True

# dfs(v)
# print()
# bfs(v)


#1520
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

mem = [[0 for _ in range(n)] for _ in range(m)] #dp를 위한 메모리
move = [[1, 0], [-1, 0], [0, 1], [0, -1]] #움직임

def dfs(a, b):
    for i in move:
        ma, mb = a + i[0], b + i[1]
        if maps[a][b] > maps[ma][mb]:
            

