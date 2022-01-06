def solution(n, edge):
    answer = 0

    dic = {}
    
    for e in edge :
        start = e[0]
        end = e[1]
        
        if start in dic :
            dic[start].append(end)
        else :
            dic[start] = [end]
        if end in dic :
            dic[end].append(start)
        else :
            dic[end] = [start]
            
    
    visited = [False for i in range(n+1)]
    visited[1] = True
    que = [[1,1]]
    result = []
    while len(que) > 0 :
        cur = que.pop(0)    
        result.append(cur)
        length = len(que)
        for num in dic[cur[0]] :
            if not visited[num] :
                visited[num] = True
                que.append([num,cur[1]+1])
    result.sort(key=lambda x : (-x[1]))
    maxVal = result[0][1]
    for r in result :
        if maxVal == r[1]:
            answer +=1
    return answer
