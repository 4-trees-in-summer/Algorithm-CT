import math

def solution(n, k):
    answer = []
    num = list(range(1,n+1))

    for i in range(n-1, 0, -1) :
        if k == 0 :
            while num :
                answer.append(num.pop())
            
            break
            
        elif k == 1 :
            while num :
                answer.append(num.pop(0))   
            
            break
        
        print(i, k)
        temp = math.factorial(i)
        if k%temp == 0 :
            answer.append(num.pop(k//(temp) -1))
        else :
            answer.append(num.pop(k//(temp)))
        k = k%temp
    
    return answer