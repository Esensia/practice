def solution(n, lost, reserve):
    answer = n
    
    lost.sort()
    new_list = list(lost)
    reserve.sort()
    for l in lost :
        if l in reserve :
            reserve.remove(l)
            new_list.remove(l)

    for l in new_list :
        answer -=1
        if l-1 in reserve :
            reserve.remove(l-1)
            answer+=1
            continue
        if l+1 in reserve :
            reserve.remove(l+1)
            answer+=1
    
    return answer
