def solution(s):
    answer = True
    
    stack = []
    for s_ in s :
        if not stack :
            stack.append(s_)
            continue
        
        if s_ == ')' :
            if not stack :
                return False
            
            stack.pop()
            continue
        
        stack.append(s_)
            
    if stack :
        return False
    return True