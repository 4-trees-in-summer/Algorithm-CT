from collections import deque

def solution(number, k):
    stack = []
    
    number = deque(number)
    
    while k > 0 :
        if stack and not number :
            stack.pop()
            k -= 1
            
        elif not stack or (number[0] <= stack[-1]) :
            stack.append(number.popleft())
            
        else :
            stack.pop()
            k -= 1
            
    if number :
        for i in number :
            stack.append(i)
            
    return ''.join(stack)