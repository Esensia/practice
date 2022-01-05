min_count = float('inf')

def compare(str1,str2) :
    count = 0
    for i in range(len(str1)) :
        if str1[i] != str2[i] :
            count+=1
        if count > 1 :
            return False
    if count == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    visited = [False for i in range(len(words))]
    if target not in words :
        return 0
    
    def dfs(word, count) :
        global min_count
        if word == target :
            min_count = min(count,min_count)
        
        for i in range(len(words)) :
            if not visited[i] and compare(word,words[i]):
                visited[i] = True
                dfs(words[i], count+1)
                visited[i] = False
    dfs(begin,0)
    
    return min_count
