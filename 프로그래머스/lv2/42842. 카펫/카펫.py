import math

def solution(brown, yellow):
    answer = []
    
    yellow_list = []
    for i in range(yellow, int(math.sqrt(yellow))-1, -1) :
        if yellow%i == 0 :
            yellow_list.append([i, yellow//i])
        
    for i,j in yellow_list :
        if (i+j)*2 + 4 == brown :
            return [i+2, j+2]
        
    return answer