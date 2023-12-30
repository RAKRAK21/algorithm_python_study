import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque()

for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    
    action = command[0]
    
    if action == 'push':
        x = command[1]
        queue.append(x)
    
    elif action == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    
    elif action == 'size':
        print(len(queue))
        
    elif action == 'empty':
        if queue:
            print(0)
        else:
            print(1)
        
    elif action == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif action == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
        
        

    