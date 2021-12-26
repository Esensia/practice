def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length 
    time = 0
    bridge_weight = 0

    while True :
        if len(truck_weights) == 0 and bridge_weight == 0 :
            break
        time += 1
        bridge_weight -= bridge[0]
        del bridge[0]
        next_num = 0
        
        if truck_weights: 
            if bridge_weight + truck_weights[0] <= weight:
                next_num = truck_weights[0]
                bridge_weight += truck_weights[0]
                del truck_weights[0]
        bridge.append(next_num)
    return time
