from collections import deque

def solution(begin, target, words):
    answer = []
    q = deque([[0, begin]])
    visited = []
    
    def differ_1(word1, word2) :
        cnt = 0
        for w1, w2 in zip(word1, word2) :
            if w1 != w2 :
                cnt += 1
                
        if cnt == 1 :
            return True
        return False
    
    while q :
        cnt, word_1 = q.popleft()
        visited.append(word_1)
        cnt += 1
        
        for word_2 in words :
            if not differ_1(word_1, word_2) or word_2 in visited :
                continue
                
            if word_2 == target :
                return cnt
            else :
                q.append([cnt, word_2])
    
    return 0
        
        
        
        
        
        