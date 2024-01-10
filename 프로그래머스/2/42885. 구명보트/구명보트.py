from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    q = deque(people)
    while q:
        if len(q) <= 1 :
            answer += 1
            break
        if q[0] + q[-1] > limit :
            q.popleft()
        else :
            q.popleft()
            q.pop()
        answer += 1
    
    return answer