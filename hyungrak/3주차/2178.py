import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, ' '.join(input().split()))) for i in range(n)]
move_a = [1, -1, 0, 0]
move_b = [0, 0, 1, -1]

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(4):
            ma = v[0] + move_a[i]
            mb = v[1] + move_b[i]
            if ma < 0 or mb < 0 or ma >= n or mb >= m:
                continue
            else:
                if miro[ma][mb] == 1:
                    miro[ma][mb] = miro[v[0]][v[1]] + 1
                    queue.append([ma, mb])

    return miro[n-1][m-1]

print(bfs([0, 0]))

