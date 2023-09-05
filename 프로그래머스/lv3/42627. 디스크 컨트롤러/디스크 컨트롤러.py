import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)
    jobs.sort(key=lambda x:(x[0], x[1]))
    
    stamp = sum(jobs[0])
    answer = jobs[0][1]

    jobs.pop(0)
    
    while jobs:
        if len(jobs) == 1:
            if stamp-jobs[0][0] <= 0 :
                answer += jobs[0][1]
                break
                
            answer += stamp-jobs[0][0] + jobs[0][1]
            break
        
        candidate = [job for job in jobs if job[0] <= stamp]

        if not candidate :
            stamp = jobs[0][0]
            print(1)
            continue
            
        candidate.sort(key = lambda x:x[1])
    
        answer += stamp-candidate[0][0] + candidate[0][1]
        stamp += candidate[0][1]
        
        jobs.remove(candidate[0])
        
    return answer//l