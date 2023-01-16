from itertools import permutations

def solution(numbers):
    answer = 0        
    words = []
    
    for i in range(1, len(numbers)+1) :
        for j in permutations(numbers, i) :
            k = int(''.join(list(j)))
            if k not in words :
                words.append(k)
    
    for i in words:
        if sosu(i) :
            answer += 1
    return answer

def sosu(num) :
    if num <= 1 :
        return False
    
    for i in range(2, num) :
        if num%i == 0 :
            return False
    
    return True
    
        