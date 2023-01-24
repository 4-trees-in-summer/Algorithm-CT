from collections import deque

def solution(s):
    answer = 0
    
    s = deque(list(s))
    
    for i in range(len(s)) :
        s.rotate(1)

        if gwalho(list(s)) :
            answer += 1
    
    return answer

def gwalho(s) :
    stack = []
    s = deque(s)
    
    while s :
        t = s.popleft()
        
        if t in '{([' :
            stack.append(t)
        elif t in ')}]' :
            if not stack :
                return False
            elif stack[-1] in '{([' :
                if t == ')' and stack[-1] == '(': 
                    stack.pop()
                elif t == '}' and stack[-1] == '{': 
                    stack.pop()
                elif t == ']' and stack[-1] == '[': 
                    stack.pop()
                else :
                    return False
            else :
                return False
    
    if stack :
        return False
    else :
        return True
    
    
    