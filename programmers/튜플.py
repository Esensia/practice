def solution(s):
    answer = []
    new_s = s.split(",{")
    new_list = []
    
    for tup in new_s :
        temp = []
        idx = 0
        string = ""
        while idx < len(tup) :
            if tup[idx].isdigit() :
                string += tup[idx]
            else :
                if len(string) > 0 :
                    temp.append(int(string))
                    string = ""
            idx +=1
        if len(string) > 0 :
            temp.append(int(string))
        new_list.append([temp,len(temp)])
    new_list.sort(key=lambda x : x[1])
    
    for i in range(len(new_list)) :
        num = new_list[i][0][0]
        answer.append(num)
        
        for j in range(i+1,len(new_list)) :
            new_list[j][0].remove(num)
    return answer
