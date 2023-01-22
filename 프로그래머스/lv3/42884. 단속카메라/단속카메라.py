def solution(routes):
    answer = 1

    routes.sort(key=lambda x : x[1])

    t = routes[0][1]
    for idx, i in enumerate(routes) :
        if t < i[0] :
            t = i[1]
            answer += 1
            
        elif i[0] >= t :
            continue
            
    return answer
