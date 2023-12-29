import sys

K = int(sys.stdin.readline().rstrip())

stack = []

for i in range(K):
    n = int(sys.stdin.readline().rstrip())
    
    if n == 0:
        stack.pop()
    
    else:
        stack.append(n)
    

if stack:
    print(sum(stack))
else:
    print(0)