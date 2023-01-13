def solution(s):
    answer = []
    cnt1 = 0
    cnt2 = 0
    
    while True :
        if s == '1' :
            break
        n1 = len(s)
        print(s)
        s = s.replace('0', '')
        print(s)
        n2 = len(s)
        cnt2 += n1-n2
        
        s = bin(n2)[2:]
        
        cnt1 += 1
        
    answer.append(cnt1)
    answer.append(cnt2)
    return answer