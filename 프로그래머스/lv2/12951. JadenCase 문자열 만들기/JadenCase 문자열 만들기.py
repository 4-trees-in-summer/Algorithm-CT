def solution(s):
    temp = 0
    answer = ''
    
    for i in s :
        if i == ' ' :
            answer += i
            temp = 0
        elif i.isalpha() :
            if temp == 0 : 
                answer += i.upper()
                temp = 1
            else :
                answer += i.lower()
        else :
            answer += i
            temp = 1
        
    return answer