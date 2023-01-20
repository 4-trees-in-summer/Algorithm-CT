def solution(numbers):
    answer = ''
    
    num_s = []
    num = list(map(str, numbers))
    
    for i in num :
        num_s.append(i*4)
        
    num_s.sort(reverse=True)
    
    for i in num_s :
        answer += i[:int(len(i)/4)]
    
    return str(int(answer))