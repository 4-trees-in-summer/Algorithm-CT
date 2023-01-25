from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    people = deque(people)
    
    while people :
        sum_ = people.popleft()
        while sum_ < limit and people:
            if sum_+people[0] > limit and sum_+people[-1] > limit :
                break
            elif sum_+people[0] <= limit :
                sum_ += people.popleft()
            elif sum_+people[-1] <= limit :
                sum_ += people.pop()
        
        answer += 1
                
    return answer