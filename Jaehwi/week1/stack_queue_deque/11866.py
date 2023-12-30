import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
sequence = deque([i+1 for i in range(N)])
answer = []

while sequence:
    sequence.rotate(-(K-1))
    answer.append(sequence.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")
