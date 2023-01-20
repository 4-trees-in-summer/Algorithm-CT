def solution(citations):
    l = len(citations)
    citations.sort()
    
    answer = 0
    
    for i in range(len(citations)) :
        if l-i <= citations[i] :
            answer = l-i
            break

    return answer