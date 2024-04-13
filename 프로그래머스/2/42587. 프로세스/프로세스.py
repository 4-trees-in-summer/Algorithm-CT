from collections import deque

def solution(priorities, location):
    answer = 0
    
    # priorities.sort(reverse = True)
    work_list = deque(list(range(len(priorities))))
    work_priorities = deque([(work, priority) for (work, priority) in zip(work_list, priorities)])
    sorted_priorities = sorted(priorities)
    cnt = 1
    while True :
        # print(cnt)
        work_ = work_priorities.popleft()
        
        if work_[1] == sorted_priorities[-1] :
            if work_[0] == location :
                return cnt
            
            sorted_priorities.pop()
            cnt += 1
        
        work_priorities.append(work_)
        
    return answer