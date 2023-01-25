import math as m

def solution(s):
    cnt_0 = 0
    cnt = 0
    a = 3
    
    while s != '1' :
        x = ''
        for i in s :
            if i == '0' :
                cnt_0 += 1
            elif i == '1':
                x += i
    
        s = str(bin(len(x))[2:])
        cnt += 1

    return [cnt, cnt_0]