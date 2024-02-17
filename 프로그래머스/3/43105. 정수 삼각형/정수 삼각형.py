def solution(triangle):
    answer = 0
    
    sum_list = [triangle[0][0]]
    for idx_1, row in enumerate(triangle[1:]) : 
        l = len(row)
        
        for idx_2, num in enumerate(row) :
            if idx_2 == 0 :
                sum_ = sum_list[0] + num
            elif idx_2 == l-1 :
                sum_ = sum_list[idx_2-1] + num
            else :
                sum_1 = sum_list[idx_2-1] + num
                sum_2 = sum_list[idx_2] + num
                sum_ = max(sum_1, sum_2)
            
            sum_list.append(sum_)
        sum_list = sum_list[l-1:]
        
    return max(sum_list)