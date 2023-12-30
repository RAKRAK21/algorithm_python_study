import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))
M = int(input())
seq_C = list(map(int, input().split()))

# 시간 제한 때문에 이중for문 사용 x
# stack은 Last In First Out 구조이기 때문에 원소를 넣었다 꺼내도 변화가 없음. 따라서 FIFO 형태의 queue만 고려.
deque = deque()
for i in range(N):
    if seq_A[i] == 0:
        deque.appendleft(seq_B[i])

for i in range(M):
    deque.append(seq_C[i])
    print(deque.popleft(), end=" ")

print("")
