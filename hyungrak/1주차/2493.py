import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
top_heights = list(map(int, input().split()))
received = []

for i in range(n):
    check = top_heights.pop()
    if top_heights[-1] >= check:
        received.append(top_heights[-1])
    elif top_heights[-1] < check:
        for j in range()
    
