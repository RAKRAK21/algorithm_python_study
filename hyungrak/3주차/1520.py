1520

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


# #1520
# import sys
# from collections import deque
# input = sys.stdin.readline

# m, n = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(m)]

# move_a = [-1, 1, 0, 0]
# move_b = [0, 0, -1, 1]


# def dfs(v):
#     stack = deque([v])
#     cnt = 0
#     while stack:
#         v = stack.pop()
#         for i in range(4):
#             ma = v[0] + move_a[i]
#             mb = v[1] + move_b[i]
#             if ma < 0 or mb < 0 or ma >= m or mb >= n:
#                 continue
#             else:
#                 if maps[ma][mb] < maps[v[0]][v[1]]:
#                     stack.append([ma, mb])
#                 if ma == m-1 and mb == n-1:
#                     stack.pop()
#                     cnt += 1
#     print(cnt)

# dfs([0, 0])

# '''시간 초과가 나오는 코드 모든 경로를 다 탐색해서 그런듯 ㅜㅜ'''
            

#1520
'''이 풀이는 다른 사람들이 일반적으로 푼 풀이랑 똑같은 듯. dfs에 dp까지 적용을 해서 푸는 것.'''
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
move_a = [-1, 1, 0, 0]
move_b = [0, 0, -1, 1]

def dfs_dp(v):
    if v[0] == m - 1 and v[1] == n - 1: #목적지는 1로
        return 1
    if dp[v[0]][v[1]] != -1: #이미 방문한 곳이면 그 값 반환
        return dp[v[0]][v[1]]
    dp[v[0]][v[1]] = 0 #방문처리 후에 뒤로가는 과정에서 그 값 추가
    for i in range(4):
        ma = v[0] + move_a[i]
        mb = v[1] + move_b[i]
        if 0 <= ma < m and 0 <= mb < n:
            if maps[ma][mb] < maps[v[0]][v[1]]: 
                dp[v[0]][v[1]] += dfs_dp([ma, mb]) #재귀호출 4개 방향으로 해서 해당위치 dp값 계속 추가
    return dp[v[0]][v[1]] #4개 방향을 모두 돌아 탐색이 끝나면 dp[v[0]][v[1]]값 리턴해서 부모 노드의 4개 방향 탐색 중 하나 완료

print(dfs_dp([0, 0]))
