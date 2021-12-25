def solution(lines):
    answer = []
    
    tup_list = []
    
    for i in range(len(lines)) :
        A = lines[i][0]
        B = lines[i][1]
        E = lines[i][2]
        for j in range(i+1,len(lines)) :
            C = lines[j][0]
            D = lines[j][1]
            F = lines[j][2]
            
            under = A*D - B*C
            if under == 0:
                continue
            up1 = B*F-E*D
            up2 = E*C-A*F
            
            if up1/under == up1//under and up2/under == up2//under :
                tup_list.append([up1//under, up2//under])
                
    minX = float('inf')
    minY = float('inf')
    
    maxX = float('-inf')
    maxY = float('-inf')
    for tup in tup_list :
        minX = min(tup[0],minX)
        minY = min(tup[1],minY)
        maxX = max(tup[0],maxX)
        maxY = max(tup[1],maxY)
    if minX < 0 :
        for tup in tup_list :
            tup[0] = tup[0] + abs(minX)
        maxX+= abs(minX)
    if minY < 0 :
        for tup in tup_list :
            tup[1] = tup[1] + abs(minY)
        maxY += abs(minY)
    if minX > 0 :
        for tup in tup_list :
            tup[0] = tup[0] - abs(minX)
        maxX-= abs(minX)
    if minY > 0 :
        for tup in tup_list :
            tup[1] = tup[1] - abs(minY)
        maxY -= abs(minY)
    
    mmap = [["." for i in range(maxX+1)] for j in range(maxY+1)]
    print(tup_list)
    for tup in tup_list :
        mmap[tup[1]][tup[0]] = "*"
    for i in range(len(mmap)) :
        answer.append("".join(mmap[i]))
    answer.reverse()
    return answer
