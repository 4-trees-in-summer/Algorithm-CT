def solution(progresses, speeds):
    answer = []
    l = len(progresses)
    visited = [False for _ in range(l)]
    ans = [0 for _ in range(l)]

    cnt = 0
    while True :
        if not False in visited :
            break
        
        cnt += 1
        for i in range(l) :
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)) :
            if progresses[i] >= 100 and not visited[i]:
                visited[i] = True
                ans[i] = cnt
                continue
        
    print(ans)
    
    temp = ans[0]
    t = 0
    for idx, day in enumerate(ans) :
        if day <= temp :
            t += 1
        elif day > temp :
            answer.append(t)
            temp = day
            t = 1
            
        if idx == len(ans)-1 :
            answer.append(t)
    
    return answer