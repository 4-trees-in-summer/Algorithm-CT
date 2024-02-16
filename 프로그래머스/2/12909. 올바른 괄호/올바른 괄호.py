def solution(s):
    answer = True
    stack = []
    for s_ in s :
        if s_ == '(' :
            stack.append(s_)
            continue
            
        if not stack :
            return False
        
        stack.pop()
    
    if stack :
        return False
    return True