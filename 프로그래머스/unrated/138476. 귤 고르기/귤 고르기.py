from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    cnt = Counter(tangerine)
    l = sorted(list(cnt.items()), key = lambda x:x[1], reverse=True)
    
    sum_ = 0
    for i in l :
        sum_ += i[1]
        answer += 1
        
        if sum_ == k :
            return answer    
        elif sum_ > k :
            return answer