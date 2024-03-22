from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    date_complete = []
    for p, s in zip(progresses, speeds) :
        date = math.ceil((100 - p)/s)
        date_complete.append(date)
    
    for idx, date in enumerate(date_complete) :
        if idx == 0 :
            max_date = date
            number_complete = 1
            continue
        
        if max_date >= date :
            number_complete += 1
            continue
        
        answer.append(number_complete)
        number_complete = 1
        max_date = date
    answer.append(number_complete)
    
    return answer