from collections import deque

n = int(input())

towers = deque([int(x) for x in input().split()])
towers.reverse()
answer = []

print(towers)

for i in range(1, n):
    if towers[i] > towers[i-1] :
        answer.append(n-i)
    # elif towers[i] == max(towers) :
    #     answer.append(0)
    else :
        answer.append('N/A')

print(answer)

answer.append(0)
answer.reverse()