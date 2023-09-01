from collections import deque

def solution(elements):
    answer = 0
    sum_list = set()
    sum_elements = sum(elements)
    elements = elements*2
    
    sum_ = 0
    for idx_sub, e1 in enumerate(elements) :
        sum_ = e1
        
        for idx_add, e2 in enumerate(elements[idx_sub+1:]) :
            sum_ = sum_+e2
            if sum_ > sum_elements :
                break
            else :
                sum_list.add(sum_)
    
    sum_list.update(set(elements))
    answer = len(sum_list)

    return answer