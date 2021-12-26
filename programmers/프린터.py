def solution(priorities, location):
    answer = 0

    result = []
    new_priorities = []
    
    for i in range(len(priorities)) :
        new_priorities.append((i,priorities[i]))
    
    while len(new_priorities) > 0 :

        temp = new_priorities.pop(0)
        isBool = False
        for j in range(0, len(new_priorities)) :
            if temp[1] < new_priorities[j][1] :
                isBool = True
                break
        if isBool :
            new_priorities.append(temp)
        else :
            result.append(temp)

    for i in range(len(result)) :

        if result[i][0] == location :
            answer = i+1
            break
    return answer
