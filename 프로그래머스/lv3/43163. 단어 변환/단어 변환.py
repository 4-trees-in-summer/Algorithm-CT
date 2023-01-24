from collections import deque

def solution(begin, target, words):
    if target not in words :
        return 0
    
    answer = 0
    
    cnt = 0
    q = deque()
    q.append([begin, cnt])

    while q :
        word, cnt = q.popleft()
        
        if word == target :
            return cnt
            
        for i in words :
            t = 0
            for idx in range(len(word)) :
                if word[idx] != i[idx] :
                    t += 1

            if t == 1:
                print(i)
                q.append([i, cnt+1])
        