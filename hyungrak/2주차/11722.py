11722

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
reversed_a = a[::-1]
mem = [1] * n

for i in range(1, n):
    for j in range(i):
        if reversed_a[i] > reversed_a[j]:
            mem[i] = max(mem[i], mem[j] + 1) 

print(max(mem))
