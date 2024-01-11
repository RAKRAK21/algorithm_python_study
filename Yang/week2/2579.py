# 2579. 계단 오르기
n = int(input())
stairs = []
score = [0 for _ in range(n)]
stairs = [int(input()) for _ in range(n)]
for i in range(n) :
    if i == 0:
        score[0] = stairs[0]
    if i == 1:
        score[1] = stairs[0] + stairs[1]
    if i > 1 :
    # else :
        score[i] = max(score[i-3] + stairs[i] + stairs[i-1], score[i-2] + stairs[i])
        
print(score[-1])
