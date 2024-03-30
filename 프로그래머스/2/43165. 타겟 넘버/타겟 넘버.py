from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    
    l = len(numbers)
    while q :
        cnt, idx = q.popleft()
        
        if idx < l-1 :
            q.append([cnt+numbers[idx+1], idx+1])
            q.append([cnt-numbers[idx+1], idx+1])
            
        elif idx == l-1 and cnt == target :
            answer += 1
    
    return answer
        
        