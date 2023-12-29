while True:
    string = input()
    stack = []
    flag = False
    
    if string == '.':
        break
    
    for char in string:
        if char == "[" or char == "(":
            stack.append(char)
            
        elif char == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            
            else:
                flag = True
                break
        
        elif char == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            
            else:
                flag = True
                break
    
    if stack or flag:
        print("no")
    else:
        print("yes")
        