def solution(msg):
    answer = []
    
    LZW = dict()
    last_num = 26
    l =  len(msg)
    for i in range(ord("A"), ord("Z")+1) :
        LZW[chr(i)] = i-64

    idx = 0
    while idx < l :
        s = msg[idx]
        for i in range(1,l) :
            if idx+i > l :
                break
                
            if msg[idx:idx+i] in LZW.keys() :
                s = msg[idx:idx+i]
                continue
            else :
                s = msg[idx:idx+i-1]
                idx_ = idx+i-1
                break
        
        answer.append(LZW[s])
        last_num += 1
        if idx <= l-2:
            LZW[msg[idx:idx_+1]] = last_num
        idx += len(s)
    
    print(LZW)
    return answer