import sys

input = sys.stdin.readline

T = int(input().rstrip())

def print_maximum(sticker, n):
    dp = [[0] * n for _ in range(2)]
    
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        return
    
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        return 
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + sticker[0][i], dp[1][i-2] + sticker[0][i])
        dp[1][i] = max(dp[0][i-1] + sticker[1][i], dp[0][i-2] + sticker[1][i])
    
    print(max(dp[0][-1], dp[1][-1]))
    
for _ in range(T):
    sticker = []
    n = int(input().rstrip())
    for _ in range(2):
        sticker.append(list(map(int, input().rstrip().split())))
    print_maximum(sticker, n)
        