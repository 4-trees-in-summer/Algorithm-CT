def solution(s):
    answer = True
    
    stack = []
    for i in s :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if not stack or stack[-1] == ')' :
                return False
            elif stack[-1] == '(' :
                stack.pop()
            
    
    if stack :
        return False 
    else :
        return True
