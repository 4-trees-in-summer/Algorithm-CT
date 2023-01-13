from collections import Counter

def solution(clothes):
    cl = []
    for i in clothes :
        cl.append(i[1])
    
    cnt = Counter(cl)
    
    answer = 1
    for i in list(cnt.values()) :
        answer *= i+1
    
    return answer-1