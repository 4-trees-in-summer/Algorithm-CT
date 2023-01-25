def solution(n):
    answer = 0
    
    number = list(range(1, n+1))
    for i in range(len(number)-1) :
        for j in range(i+1, len(number)+1) :
            sum_ = sum(number[i:j])
            if sum_ == n :
                answer += 1
                break
            elif sum_ > n :
                break
    
    return answer+1