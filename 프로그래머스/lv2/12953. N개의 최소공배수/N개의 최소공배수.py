import math

def solution(arr):
    ans = []
    answer = arr[0]
    
    for i in arr[1:] :
        t = max(answer, i)
        
        for j in range(t, answer*i+1) :
            if j%answer == 0 and j%i == 0 :
                answer = j
                break
        
    return answer