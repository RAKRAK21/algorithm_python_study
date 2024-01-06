import sys

input = sys.stdin.readline

N = int(input().rstrip())
sequence =  list(map(int, input().rstrip().split()))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = 1
    else:
        maximum = [0]
        for j in range(i):
            if sequence[j] > sequence[i] and dp[j]+1 > maximum[0]:
                maximum = [dp[j]+1]
        if maximum == [0]:
            dp[i] = 1
        else:
            dp[i] = maximum[0]
         
print(max(dp))