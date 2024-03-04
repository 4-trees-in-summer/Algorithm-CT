from collections import deque

def solution(priorities, location):
    answer = 1
    
    l = len(priorities)
    prior_list = deque(sorted(priorities, reverse = True))
    priorities = deque(priorities)
    
    while priorities :
        if priorities[0] != prior_list[0] :
            priorities.append(priorities[0])
            priorities.popleft()
                        
            location -= 1
            if location < 0 :
                location += len(priorities)
            continue
        
        if location != 0 :
            priorities.popleft()
            prior_list.popleft()
            
            location -= 1
            answer += 1
            continue
        
        return answer