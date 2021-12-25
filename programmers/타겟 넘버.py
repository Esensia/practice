result = 0
list_num = []
visited = []

def dfs(ix,count, cur_val,target) :
    
    if count == len(list_num) :
        global result
        if cur_val == target:
            result += 1
        return

    for i in range(ix,len(list_num)) :

        if visited[i] == False :
            visited[i] == True
            dfs(i+1,count+1, cur_val-list_num[i],target)
            dfs(i+1,count+1, cur_val+list_num[i],target)
            visited[i] = False

def solution(numbers, target):

    for num in numbers :
        list_num.append(num)
        visited.append(False)
    
    dfs(0,0,0,target)
    
    return result
