import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    order = sys.stdin.readline().rstrip().split()
    if len(order) == 1:
        func = int(order[0])
    else:
        func = int(order[0])
        x = int(order[1])
        
    if func == 1:
        stack.append(x)

    elif func == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif func == 3:
        print(len(stack))

    elif func == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif func == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)     