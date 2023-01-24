import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K :
        return 0
    
    cnt = 0
    while len(scoville) >= 2 :
        cnt += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        
        n_s = s1+s2*2
        heapq.heappush(scoville, n_s)
        
        if scoville[0] >= K :
            return cnt  

    return -1