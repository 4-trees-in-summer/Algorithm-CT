def solution(s):
    answer = True
    
    stack = []
    for s_ in s :
        if s_ == '(' :
            stack.append(s_)
        else :
            if not stack :
                return False
            
            if stack[-1] == '(' :
                stack.pop()
    if stack :
        return False
    return True