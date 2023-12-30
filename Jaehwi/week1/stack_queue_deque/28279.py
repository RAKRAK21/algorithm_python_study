# deque는 stack과 queue의 역할 모두를 수행할 수 있는 자료 구조
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

mydeque = deque()

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    action = int(command[0])

    if action == 1:
        x = int(command[1])
        mydeque.appendleft(x)

    elif action == 2:
        x = int(command[1])
        mydeque.append(x)

    elif action == 3:
        if mydeque:
            print(mydeque.popleft())
        else:
            print(-1)

    elif action == 4:
        if mydeque:
            print(mydeque.pop())
        else:
            print(-1)

    elif action == 5:
        print(len(mydeque))

    elif action == 6:
        if mydeque:
            print(0)
        else:
            print(1)

    elif action == 7:
        if mydeque:
            print(mydeque[0])
        else:
            print(-1)

    elif action == 8:
        if mydeque:
            print(mydeque[-1])
        else:
            print(-1)