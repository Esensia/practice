num_list = []
visited = [False] * 30
answer = 0

def dfs(count,idx):
    global answer
    if count != 0 :
        mul = 1
        for i in range(len(num_list)) :
            if visited[i] :
                mul *= num_list[i]  
        answer += mul
    if count == len(num_list) :
        return
    for i in range(idx,len(num_list)) :
        if visited[i] == False :
            visited[i] = True
            dfs(count+1,i)
            visited[i] = False

def solution(clothes):
    
    dic = {}

    for clothe in clothes :
        parts = clothe[1]
        if hash(parts) in dic :
            dic[hash(parts)] = dic[hash(parts)]+1 # 해시함수 안써도됨
        else :
            dic[hash(parts)] = 1

    global num_list
    num_list = list(dic.values())
    
    #dfs(0,0) dfs로 할 시 모든 옷의 종류가 하나씩 있는경우 시간초과 2**30 - 1
    
    #경우의 수가 [A,B,C]가 있으면
    #옷을 입는 경우의 수는 A*B*C
    #A만 선택하고 B와 C는 선택하지 않는 경우가 있기때문에 각각 1씩 더해준다 (한가지는 반드시 입어야하기 때문)
    #(A+1)(B+1)(C+1)
    #여기서 모든 옷을 안입는 경우가 있으므로 -1을 해준다
    
    mul=1
    for num in num_list:
        mul *= (num+1)
    return mul -1
