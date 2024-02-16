def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    last_num = -1
    for num in arr :
        if num == last_num :
            continue
        
        last_num = num
        answer.append(num)
    
    return answer