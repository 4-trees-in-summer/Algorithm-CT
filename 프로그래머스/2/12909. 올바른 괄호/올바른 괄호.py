from collections import deque

def solution(s):
    answer = True
    s = deque(list(s))
    
    stack = []
    while s :
        if not stack :
            if s[0] == ')' :
                print(1)
                
                return False
            stack.append(s.popleft())
            continue
        
        if stack[-1] == s[0] :
            stack.append(s.popleft())
            continue
        
        stack.pop()
        s.popleft()
    
    if stack :
        return False
    
    return True