import math
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1: # 1은 소수가 아님
        continue
    
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0: # 판단하는 수(i)가 j로 나누었을 때 나머지가 0이면 약소가 있는 것이므로 소수가 아님
            break
    
    else: #위의 것들에 해당하지 않는 수들은 소수
        print(i)
    
'''이번 문제에서는 이 풀이가 맞기는 했지만.. 개인적으로 시간을 줄이는 방법이 있을 것 같다는 생각이 든다. 한번 생각해보자.'''