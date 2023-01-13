def solution(participant, completion):
    participant.sort()
    completion.sort()

    l = len(completion)
    
    for i in range(l) :
        if participant[i] != completion[i] :
            return participant[i]
    
    return participant[-1]
            
