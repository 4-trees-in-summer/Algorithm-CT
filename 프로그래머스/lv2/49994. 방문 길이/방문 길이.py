def solution(dirs):
    road = []
    start, end = 0, 0
    
    for i in dirs :
        if i == 'U' :
            if end+1 > 5 :
                continue
            if [start, end, start, end+1] not in road :
                road.append([start, end, start, end+1])
                road.append([start, end+1, start, end])
            end += 1
                
        elif i == 'D' :
            if end-1 < -5 :
                continue
                
            if [start, end, start, end-1] not in road :
                road.append([start, end, start, end-1])
                road.append([start, end-1, start, end])
            end -= 1
            
        elif i == 'R' :
            if start+1 > 5 :
                continue
                
            if [start, end, start+1, end] not in road :
                road.append([start, end, start+1, end])
                road.append([start+1, end, start, end])
            start += 1
            
        elif i == 'L' :
            if start-1 < -5 :
                continue
                
            if [start, end, start-1, end] not in road :
                road.append([start, end, start-1, end])
                road.append([start-1, end, start, end])
            start -= 1

    return len(road)//2