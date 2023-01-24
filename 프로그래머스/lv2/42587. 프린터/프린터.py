from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, i in enumerate(priorities) :
        q.append([i, idx])
        
    cnt = 1
    while q :
        if len(q) == 1 :
            return cnt
        
        if q[0][0] >= max([num[0] for num in list(q)[1:]]) :
            if q[0][1] == location :
                return cnt
            else :
                q.popleft()
                cnt += 1
        else :
            q.rotate(-1)
            
