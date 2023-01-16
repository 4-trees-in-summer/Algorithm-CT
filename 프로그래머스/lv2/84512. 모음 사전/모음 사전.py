from itertools import product

def solution(word):
    answer = 0
    
    ans = ''
    words = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6) :
        for j in product(alpha, repeat = i) :
            words.append(''.join(list(j)))
    
    words.sort()
    answer = words.index(word)+1

    return answer