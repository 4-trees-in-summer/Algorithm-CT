def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    t = 0
    
    bridge_sum = 0
    
    while bridge :
        t += 1
        w = bridge.pop(0)
        bridge_sum -= w
        
        if truck_weights :
            if bridge_sum +  truck_weights[0] <= weight :
                w = truck_weights.pop(0)
                bridge.append(w)
                
                bridge_sum += w
        
            else :
                bridge.append(0)
        
    return t 