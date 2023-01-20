def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        idx = 0
        t = True
        for i in tree :
            if idx == len(skill) :
                break
                
            if i == skill[idx] :
                idx += 1
            elif i in skill[idx+1:] :
                t = False
                break
        
        if t == True :
            answer += 1

    return answer