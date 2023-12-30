import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
yose = deque([a for a in range(1, n+1)])
ans = []

for i in range(n):
    yose.rotate(-1 * (k-1))
    ans.append(yose.popleft())

print("<"+", ".join(map(str, ans))+">")