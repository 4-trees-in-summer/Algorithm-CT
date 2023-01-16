from itertools import permutations

def solution(k, dungeons):
    answer = []
    orig_k = k
    dun_list = list(permutations(dungeons, len(dungeons)))
    
    for i in dun_list :
        k = orig_k
        cnt = 0
        for j in i :
            if j[0] <= k :
                k -= j[1]
                cnt += 1
                
                if cnt == len(dungeons) :
                    return cnt
            else :
                answer.append(cnt)
                break

    return max(answer)