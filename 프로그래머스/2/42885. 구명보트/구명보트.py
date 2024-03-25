from collections import deque

def solution(people, limit):
    answer = 0
            
    people.sort()
    q = deque(people)
    
    while q :
        if len(q) == 1 :
            answer += 1
            break
            
        maxi = q.pop()
        mini = q[0]
        
        if mini+maxi <= limit :
            q.popleft()
        
        answer += 1 
        
    return answer