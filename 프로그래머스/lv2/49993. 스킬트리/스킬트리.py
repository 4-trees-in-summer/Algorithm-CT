def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees :
        skill_ = list(skill)

        for i in s :
            if skill_ and i == skill_[0] :
                skill_.pop(0)

            elif len(skill_) >= 2 :
                if i in skill_[1:] :
                    break
        else :
            answer += 1
                
                
    return answer