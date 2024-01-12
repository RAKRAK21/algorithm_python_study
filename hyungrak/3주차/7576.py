import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
ans = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])


while queue:
    k = queue.popleft()
    for i in range(4):
        dx = k[0] + x[i]
        dy = k[1] + y[i]
        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue
        elif tomato[dx][dy] == 0:
            tomato[dx][dy] = tomato[k[0]][k[1]] + 1
            queue.append([dx, dy])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, tomato[i][j])
    
print(ans-1)


