9252

import sys

input = sys.stdin.readline

str_a = input().rstrip()
str_b = input().rstrip()
la = len(str_a)
lb = len(str_b)
mem = [['' for _ in range(la+1)] for _ in range(lb+1)] #범위를 딱맞게 했더니 index error가 남
'''dp 표를 이용함. '''

for i in range(1, lb+1):
    for j in range(1, la+1):
        if str_a[j-1] == str_b[i-1]:
            mem[i][j] = mem[i-1][j-1] + str_a[j-1]
        else:
            if len(mem[i-1][j]) >= len(mem[i][j-1]):
                mem[i][j] = mem[i-1][j]
            else:
                mem[i][j] = mem[i][j-1]

ans = mem[-1][-1] #이거를 해주고 안해주고 차이에서 시간초과가 나냐 안나나가 결정됨 ㅇㅅㅇ.. 왤까??
            
print(len(ans), ans, sep="\n")

