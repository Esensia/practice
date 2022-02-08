def solution(id_list, report, k):
    answer = []
    
    s = set()
    dic = {}
    dic2 = {}
    for id in id_list :
        dic[id] = []
        dic2[id] = 0
    
    for i in report :
        s.add(i)

    for re in s :
        names = re.split(" ")
        dep = names[0]
        des = names[1]
        
        dic[dep].append(des)
        dic2[des] = dic2[des]+1
        
    for id in id_list :
        count = 0
        new_list = dic[id]
        for l in new_list :
            if dic2[l] >= k :
                count+=1
        answer.append(count)
                
            
    return answer
