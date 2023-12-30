import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
balloons = sys.stdin.readline().rstrip().split()
balloons = deque([[idx+1, int(val)] for idx, val in enumerate(balloons)])
result = []

# 자기 자신을 없애고 가기 때문에 값이 0보다 클땐 1빼주기 (rotate 시 -부호 붙여서 돌기)
while balloons:
    value = balloons.popleft()
    result.append(value[0])
    if value[1] > 0:
        balloons.rotate(-(value[1]-1))
    else:
        balloons.rotate(-value[1])
print(*result, sep=" ")
