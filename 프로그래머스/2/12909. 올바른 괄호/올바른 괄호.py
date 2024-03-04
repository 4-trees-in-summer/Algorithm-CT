def solution(s):
    answer = True
    
    stack = []
    stack_check = []
    for s_ in s :
        stack.append(s_)
    
    while stack :
        if stack[-1] == '(' :
            if not stack_check  :
                return False
            stack.pop()
            stack_check.pop()
            continue
        
        stack_check.append(stack.pop())
    
    if stack_check :
        return False
    
    return True