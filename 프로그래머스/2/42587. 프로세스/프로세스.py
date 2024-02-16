from collections import deque

def solution(priorities, location):
    answer = 0
    q_priorities = deque(priorities)
    
    priorities.sort(reverse = True)
    priorities = deque(priorities)
    
    l = len(priorities)
        
    prior_idx = 0
    cnt = 0
    while q_priorities :
        if q_priorities[0] == priorities[0] :
            q_priorities.popleft()
            priorities.popleft()

            cnt += 1
            
            if location != 0 :
                location -= 1
                continue
                                
            return cnt
    
        q_priorities.rotate(-1)

        location -= 1
        if location == -1 :
            location += len(priorities)
        
    return cnt