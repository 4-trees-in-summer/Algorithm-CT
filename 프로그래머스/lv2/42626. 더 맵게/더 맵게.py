import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for i in scoville :
        heapq.heappush(heap, i)
    
    cnt = 0
    while heap[0] < K :
        if len(heap) >= 2:        
            cnt += 1
            
            ans = heapq.heappop(heap)
            ans += heapq.heappop(heap)*2
            
            heapq.heappush(heap, ans)              
            
        elif len(heap) == 1:
            return -1            
    
    return cnt