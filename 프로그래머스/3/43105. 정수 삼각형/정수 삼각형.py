def solution(triangle):
    answer = 0
    
    for h in range(1, len(triangle)) :
        length = len(triangle[h])
        
        for idx in range(length) :
            # print(h, idx)
            if idx == 0 :
                triangle[h][idx] += triangle[h-1][idx]
            elif idx+1 == length:
                triangle[h][idx] += triangle[h-1][idx-1]
            else:
                triangle[h][idx] += max(triangle[h-1][idx-1], triangle[h-1][idx])
        
    return max(triangle[-1])