def solution(record):
    answer = []
    
    dic = {}
    result = []
    for r in record :
        s = r.split(" ")
        if len(s) == 3:
            order = s[0]
            id = s[1]
            name = s[2]
        else :
            order = s[0]
            id = s[1]
        if order == "Enter" :
            dic[id] = name
            result.append((1,id))

        elif order == "Leave":
            result.append((2,id))
        else :
            dic[id] = name

    for ord,i in result :
        str = dic[i]+"님이 "
        if ord == 1 :
            str += "들어왔습니다."
        else :
            str += "나갔습니다."
        answer.append(str)

    return answer
