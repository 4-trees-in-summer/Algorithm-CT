from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dic = defaultdict(list)
    cnt_dic = dict()
    
    for idx in range(len(genres)) :
        dic[genres[idx]].append([plays[idx], idx])
    
    for i in dic :
        cnt_dic[i] = sum(cnt for cnt, idx in dic[i])
        
        print(dic[i])
        dic[i].sort(key = lambda x:x[1])
        print(dic[i])
        dic[i].sort(key = lambda x:x[0],reverse=True)
        print(dic[i])

    temp = sorted(list(cnt_dic.items()), key = lambda x:x[1], reverse=True)
    
    for i, cnt in temp :
        if len(dic[i]) >= 2 :
            answer.append(dic[i][0][1])
            answer.append(dic[i][1][1])
        else :
            answer.append(dic[i][0][1])
        
    return answer