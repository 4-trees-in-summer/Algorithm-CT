from collections import defaultdict

def solution(fees, records):
    
    car = defaultdict(list)
    
    for record in records :
        record = record.split()
        car[record[1]].append(record[0].replace(':', ''))
        
    keys = sorted(list(car.keys()))
    
    answer = [0 for i in range(len(keys))]
    for ans, num in enumerate(keys) :
        if len(car[num])%2 == 1 :
            car[num].append('2359')
            
        time_h, time_m = 0, 0
        for idx, t in enumerate(car[num]) :
            if idx%2 == 0 :
                continue
            time_h += int(car[num][idx][:2]) - int(car[num][idx-1][:2])
            time_m += int(car[num][idx][2:]) - int(car[num][idx-1][2:])
        
        
        time = time_h*60 + time_m
            
        answer[ans] += fees[1]
        if time > fees[0] :
            if (time-fees[0])%fees[2] == 0:
                answer[ans] += fees[3]*((time-fees[0])//fees[2])
            else :
                answer[ans] += fees[3]*(((time-fees[0])//fees[2])+1)

    return answer