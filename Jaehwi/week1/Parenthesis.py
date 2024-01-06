T = int(input())
input_string = []

for i in range(T):
    input_string.append(input())

for seq in range(T):
    stack = []
    flag = False
    for character in input_string[seq]:
        if character == "(":
            stack.append("(")
        
        elif character == ")":
            try:
                stack.pop()
            
            except:
                flag = True
                break
            
    if stack or flag:
        print("NO")
    else:
        print("YES")