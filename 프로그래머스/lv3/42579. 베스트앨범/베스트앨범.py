def solution(genres, plays):
    answer = []
    
    genres_set = list(set(genres))
    
    play_list = [[] for _ in range(len(genres_set))]
    play_sum = [0 for _ in range(len(genres_set))]
    
    for i in range(len(plays)) :
        ind = genres_set.index(genres[i])
        play_list[ind].append([i, plays[i]])
        play_sum[ind] += plays[i]
        
    for i in play_list :
        i.sort(key = lambda x : x[1], reverse=True)
        
    for i in range(len(genres_set)) :
        p = play_sum.index(max(play_sum))
        
        if len(play_list[p]) != 1 :
            answer.append(play_list[p][0][0])
            answer.append(play_list[p][1][0])
        elif len(play_list[p]) == 1 :
            answer.append(play_list[p][0][0])
        
        play_sum.pop(p)
        play_list.pop(p)


    return answer