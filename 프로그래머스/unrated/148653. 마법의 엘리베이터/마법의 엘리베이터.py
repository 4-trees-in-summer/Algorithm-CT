def solution(storey):
    answer = 0
    
    i = 0
    while storey > 0 :
        num = storey%10
        
        if num < 5 :
            answer += num
            storey -= num
            storey = storey//10

        elif num > 5:
            answer += 10 - num
            storey += 10 - num
            storey = storey//10
        
        elif num == 5 :
            if (storey//10)%10 >= 5 :
                answer += num
                storey += 5
                storey = storey//10
            else :
                answer += num
                storey -= 5
                storey = storey//10

            
    return answer