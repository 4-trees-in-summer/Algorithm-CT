from collections import deque

def solution(operations):
    answer = []
    ans = deque()
    
    for i in operations :
        if i[0] == 'I' :
            ans.append(int(i[1:].lstrip()))
        elif i == 'D 1' and len(ans) != 0 :
            ans.remove(max(ans))
        elif i == 'D -1' and len(ans) != 0 :
            ans.remove(min(ans))
    
    
    if ans :
        return [max(ans), min(ans)]
    else:
        return [0, 0]