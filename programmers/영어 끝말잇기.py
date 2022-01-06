def solution(n, words):
    answer = []
    i = 1
    match = 1
    dic = {}
    pre = words[0][0]
    for word in words :
        if i > n :
            i=1
            match +=1
        if word in dic or pre != word[0]:
            answer.extend([i,match])
            break
        else :
            dic[word] = ""
        i+=1
        pre = word[-1]
        
    if len(answer) == 0:
        answer = [0,0]
    return answer
