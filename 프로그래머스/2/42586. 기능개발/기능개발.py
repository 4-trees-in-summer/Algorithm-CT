import math

def solution(progresses, speeds):
    answer = []
    
    end_day = 0
    for day, (progress, speed) in enumerate(zip(progresses, speeds)) :
        temp = math.ceil((100 - progress)/speed)

        if day == 0 :
            answer.append(1)
            end_day = temp
            continue
            
        if temp <= end_day :
            answer[-1] += 1
        else :
            answer.append(1)
            end_day = temp
        
        
    return answer