import math

def solution(progresses, speeds):
    answer = []
    
    # 걸리는 시간 계산
    end_day = []
    for p, s in zip(progresses, speeds) :
        end_day.append(math.ceil((100-p)/s))
    
    # 그걸 바탕으로 계산
    before_day = end_day[0]
    solution = 1
    
    for d in range(1, len(end_day)) :            
        if end_day[d] <= before_day :
            solution += 1
            continue
        
        answer.append(solution)
        
        solution = 1
        before_day = end_day[d]
        
    answer.append(solution)
    
    return answer