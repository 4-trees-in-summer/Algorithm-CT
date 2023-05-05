def solution(numbers):
    answer = []
      
    for num in numbers :
        if num%2 == 0 :
            answer.append(num+1)
        else :
            two_ = '0'+bin(num)[2:]
            
            for i, idx in enumerate(range(len(two_)-1, -1, -1)) :
                if two_[idx] == '0' :
                    two_ = two_[:idx]+'1'+two_[idx+1:]
                    answer.append(int(two_,2)-2**(i-1))
                    break

    return answer