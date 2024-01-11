'''
import sys

input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()

dp = [0] * len(seq_1)

for i in range(len(seq_1)):
    if i == 0 and seq_1[i] in seq_2:
        dp[i] = [[seq_1[i]], [seq_2.find(seq_1[i])]]
    else:
        max = [0, [0]]
        for j in range(i):
            # 문자열과, 마지막 index 번호가 묶임
            for idx, pair in enumerate(zip(dp[j][0], dp[j][1])):
                left_seq = seq_2[pair[1]+1:]
                if seq_1[i] in left_seq:
                    if len(pair[0])+1 > max[0]:
                        max = [len(pair[0])+1, [(j,idx)]]
                    elif len(pair[0])+1 == max[0]:
                        max[1].append((j, idx))
        if max[0] == 0:
            dp[i] = [[seq_1[i]], [seq_2.find(seq_1[i])]]
        else:
            for idx, value in enumerate(max[1]):
                last_index = dp[value[0]][1][value[1]]
                string = dp[value[0]][0][value[1]]
                left_seq = seq_2[last_index+1:]
                find_idx = left_seq.find(seq_1[i]) + last_index + 1
                if idx == 0:
                    dp[i] = [[string+seq_1[i]], [find_idx]]
                else:
                    dp[i][0].append(string+seq_1[i])
                    dp[i][1].append(find_idx)

maximum = ""
for string in dp:
    if len(string[0][0]) > len(maximum):
        maximum = string[0][0]

print(len(maximum))
print(maximum)

O(N^3) 시간 초과 -> 이문제의 경우 최대 O(N^2logN)안에서 끝내야 함.
'''


import sys

input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()

table = [['' for _ in range(len(seq_1)+1)] for _ in range(len(seq_2)+1)]

for row in range(1, len(seq_2)+1):
    for column in range(1, len(seq_1)+1):
        if seq_2[row-1] == seq_1[column-1]:
            table[row][column] = table[row-1][column-1] + seq_2[row-1]
        else:
            if len(table[row][column-1]) >= len(table[row-1][column]):
                table[row][column] = table[row][column-1]
            else:
                table[row][column] = table[row-1][column]

value = table[-1][-1]
print(len(value))
print(value)
