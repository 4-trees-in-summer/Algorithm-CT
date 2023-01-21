def solution(N, stages):
    answer = []
    
    fail = []
    all_player = len(stages)
    
    for i in range(1, N+1) :
        player = stages.count(i)
        fail.append([player/all_player, i])
        
        if all_player - player > 0 :
            all_player -= player

    fail.sort(key = lambda x:x[0], reverse=True)
    
    for i in fail :
        answer.append(i[1])
        
    return answer