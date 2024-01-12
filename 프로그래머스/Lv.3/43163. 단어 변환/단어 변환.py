from collections import deque

def differ_1(s1, s2) :
    cnt = 0
    for s_1, s_2 in zip(s1, s2) :
        if cnt >= 2:
            break
        if s_1 == s_2 :
            continue
        cnt += 1
        
    if cnt == 1 :
        return True
    else :
        return False
    
def solution(begin, target, words):
    answer = 0
    visited = []
    q = deque()
    
    distance = 0
    q.append([begin, distance])
    while q:
        word_1, distance = q.popleft()
        visited.append(word_1)
        
        for word_2 in words :
            if not differ_1(word_1, word_2) :
                continue
            
            if word_2 != target :
                if word_2 not in visited :
                    q.append([word_2, distance+1])
                continue
            
            return distance+1
    
    return 0