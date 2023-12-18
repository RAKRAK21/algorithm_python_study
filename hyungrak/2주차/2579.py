import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * 301
dp = [0] * 301

for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, n):
    dp[i] = (max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i]))
    
print(dp[n-1])


#2579 런타임 에러 코드
# import sys
# input = sys.stdin.readline

# n = int(input())
# stair = []

# for i in range(n):
#     stair.append(int(input()))

# dp = [stair[0], stair[0] + stair[1], max(stair[0] + stair[2], stair[1] + stair[2])]
# for i in range(3, n):
#     dp.append(max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i]))
    
# print(dp[-1])

'''이 코드는 왜 런타임 에러가 뜰까???? ㅜㅜ'''