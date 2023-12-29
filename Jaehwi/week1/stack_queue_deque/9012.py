import sys

T = int(sys.stdin.readline().rstrip())


for i in range(T):
    string = sys.stdin.readline().rstrip()
    stack = []
    flag = False
    
    for char in string:
        if char == '(':
            stack.append('(')
        
        elif char == ')':
            try:
                stack.pop()
            
            except:
                flag = True
                break
                
    if stack or flag:
        print("NO")
    else:
        print("YES")
        
        
        