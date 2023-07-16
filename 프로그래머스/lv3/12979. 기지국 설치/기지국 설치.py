def solution(n, stations, w):
    answer = 0
    apt = []
    length = 2*w+1
    start = 1
    for station in stations :
        station_start = station-w
        station_end = station+w
        
        if station_start > start :
            apt.append(station_start - start)
        
        start = station_end + 1
    
    if station_end < n :
        apt.append(n-station_end)
        
    print(apt)
    for a in apt :
        answer += a//length if a%length == 0 else a//length + 1
        print(answer)
        
    return answer