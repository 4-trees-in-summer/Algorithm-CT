from collections import Counter

def solution(s):
    answer = []
    num_list = {}
    num = ''
    
    for i in s :
        if i.isdigit() :
            num += i
        
        else :
            if num.isdigit() :
                if num not in num_list :
                    num_list[num] = 1
                else :
                    num_list[num] += 1
                    
            num = ''
        
    l = list(num_list.items())
    l.sort(key = lambda x : x[1], reverse=True)
    
    for i in l :
        answer.append(int(i[0]))
        
    return answer