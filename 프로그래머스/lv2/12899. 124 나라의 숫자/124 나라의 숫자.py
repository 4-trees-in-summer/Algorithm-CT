def solution(n):
    answer = ''
    stack = []
    
    while True :
        if n < 3 :
            stack.append(n)
            break
        elif n == 3:
            stack.append(n)
            break
            
        k = n%3
        n = n//3
        
        if k == 0 :
            n = n-1
            
        stack.append(k)
    
    while stack :
        num = stack.pop()
        
        if num == 1 :
            answer += '1'
        elif num == 2 :
            answer += '2'
        else :
            answer +='4'
    
    return answer


'''
11 42
12 44

13 111
14 112
15 114

16 121
17 122
18 124
'''