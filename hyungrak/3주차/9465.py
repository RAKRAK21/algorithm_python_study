import sys

input = sys.stdin.readline

t = int(input())
ans = []

def dp (n, sticker):
    if n == 1:
        return max(sticker[0][0], sticker[1][0])
    elif n == 2:
        return max(sticker[0][1] + sticker[1][0], sticker[1][1] + sticker[0][0])
    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        for i in range(2, n):
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    return max(sticker[0][n-1], sticker[1][n-1])

for i in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    ans.append(dp(n, sticker))

print(*ans, sep="\n")