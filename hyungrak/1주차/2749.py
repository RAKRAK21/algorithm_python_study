#2747
'''import sys

input = sys.stdin.readline

n = int(input())

def fibo(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))

2747번을 먼저 풀어봤는데 안타깝게도 재귀로 하니까 시간 초과가 났다.
'''

#2747
'''import sys

input = sys.stdin.readline

n = int(input())
fibo_list = [0] * (n+1)
fibo_list[1] = 1

for i in range(2, n+1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[n])

for문으로 해결함.
'''

#2749
'''import sys
input = sys.stdin.readline

n = int(input())
k = int(n % (15 * 100000))
fibo_list = [0] * (k+1)
fibo_list[1] = 1

for i in range(2, k+1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[k] % 1000000)

메모리 초과
'''

import sys
input = sys.stdin.readline

n = int(input())
k = int(n % (15 * 100000))
fibo_list = [0, 1]

for i in range(2, k+1):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    fibo_list[-1] = fibo_list[-1] % 1000000
print(fibo_list[k]) 
