visited = [False] * 2000
new_set = set()
cour = []
def dfs(idx,order) :
    s = ""
    global new_list
    for i in range(len(order)) :  
        if visited[i] :
            s += order[i]
    if len(s) in cour :
        new_set.add((''.join(sorted(s)), len(s) ))
    
    for i in range(idx, len(order)) : # Python combination 라이브러리좀 써라;;
        if visited[i] == False:
            visited[i] = True
            dfs(i+1,order)
            visited[i] = False

def solution(orders, course):
    answer = []
    global cour 
    cour = course
    global new_set
    local_set = set()
    for order in orders :
        visited = [False] * 2000
        dfs(0,order)
        local_set = local_set | new_set
        new_set = set()
    new_list = list(local_set)
    new_list.sort(key=lambda x : x[1])
    result = []
    for tup in new_list :
        count = 0
        maxcount = 0
        for order in orders :
            check = 1
            
            for s in tup[0] :
                if s not in order :
                    check = 0
                    break
            if check == 1:
                count +=1
        if count > 1 and maxcount <= count:
            maxcount = count
            result.append( (tup[0],count,tup[1]))
    result.sort(key=lambda x : (x[2],-x[1]))
    length = result[0][2]
    c = result[0][1]
    
    for r in result :
        if length != r[2]:
            length = r[2]
            c = r[1]
        if c == r[1] :
            answer.append(r[0])
    answer.sort()
    return answer
