from collections import deque

def solution(priorities, location):
    answer = 1
    
    sorted_priorities = deque(sorted(priorities, reverse = True))
    priorities = deque(priorities)
    
    do_pop = False
    while True :
        if sorted_priorities[0] != priorities[0] :
            priorities.rotate(-1)
            location -= 1
            
            if location < 0 :
                location += len(priorities)
            continue
        
        if location != 0 :
            answer += 1
            sorted_priorities.popleft()
            priorities.popleft()
            
            location -= 1
            
            if location < 0 :
                location += len(priorities)
            continue
        
        if location == 0 :
            break
    
    return answer