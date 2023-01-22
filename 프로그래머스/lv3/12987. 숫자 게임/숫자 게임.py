from collections import deque

def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    A = deque(A)
    B = deque(B)
    
    if A[-1] >= B[0] :
        return 0
    
    for i in A :
        if not B :
            break
            
        if i < B[0] :
            answer += 1
            B.popleft()
            
        elif i == B[0] :
            B.pop()
            
        else :
            B.pop()
            
    return answer