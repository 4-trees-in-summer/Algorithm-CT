from itertools import combinations

def solution(orders, course):
    answer = []
    
    # print(list(combinations(orders[0], 2)))
    for c in course :
        result_list = []
        for order in orders :
            combi = list(combinations(order, c))
            result_list += list(map(lambda tup: ''.join(sorted(tup)), combi))
        
        result_distinct = list(set(result_list))

        maxi = 0
        ans = []
        for r in result_distinct :
            count_ = result_list.count(r) 
            
            if maxi > count_ :
                continue
            elif count_ == 1 :
                continue
            elif maxi == count_ :
                ans.append(r)
            else :
                maxi = count_
                ans = []
                ans.append(r)
        
        answer += ans

    return sorted(answer)