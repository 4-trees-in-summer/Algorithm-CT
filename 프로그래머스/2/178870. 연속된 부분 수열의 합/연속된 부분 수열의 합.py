from collections import deque

def solution(sequence, k):
    answer = []
    
    idx_front = 0
    idx_rear = 0
    cnt = sequence[0]
    min_len = len(sequence)
    if sequence[0] == k :
        return [0, 0]
    
    if sequence[-1] == k :
        return [len(sequence)-1, len(sequence)-1]
    
    while idx_front < len(sequence)-1:
    # for _ in range(len(sequence)) :
        if cnt < k :
            if idx_rear == len(sequence) - 1 :
                idx_front += 1
                cnt -= sequence[idx_rear]
                
            else :
                idx_rear += 1
                cnt += sequence[idx_rear]
            
        elif cnt > k :
            cnt -= sequence[idx_front]
            idx_front += 1
            
        else :
            if idx_rear - idx_front < min_len :
                answer = [idx_front, idx_rear]
                min_len = idx_rear - idx_front
                # print('-', [idx_front, idx_rear])
                
                
            cnt -= sequence[idx_front]
            idx_front += 1
                
        # print([idx_front, idx_rear], cnt)
            
    return answer