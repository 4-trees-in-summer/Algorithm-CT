from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for permu in permutations(dungeons, len(dungeons)) :
        k_ = k
        cnt = 0
        
        for idx, dungeon in enumerate(permu) :
            if dungeon[0] <= k_ and k_ >= dungeon[1] :
                k_ -= dungeon[1]
                cnt += 1
                
                if idx == len(dungeons)-1 :
                    answer.append(cnt)
                    break
            else :
                answer.append(cnt)
                break
        
    return max(answer)