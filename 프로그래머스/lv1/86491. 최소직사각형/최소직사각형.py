def solution(sizes):
    answer = 0
    list1 = []
    list2 = []
    
    for i in sizes :
        if i[0] < i[1] :
            i[0], i[1] = i[1], i[0]
        
        list1.append(i[0])
        list2.append(i[1])
            
    answer = max(list1)*max(list2)

    return answer