#
def check(str_u) :
    count = 0
    for s in str_u :
        if s == "(":
            count += 1
        else :
            count -= 1
        if count < 0 :
            return False
    return True

def func(str_p) :
    answer = ""
    count = 0
    u = ""
    idx = 0
    for i in range(len(str_p)) :
        
        if str_p[i] == "(":
            count+=1
        else :
            count-=1
        if count == 0 :
            idx = i
            break
    
    u = str_p[:idx+1]
    v = str_p[idx+1:]
    
    if check(u) :
        answer += u
    else :
        answer += "("
        if v != "":
            answer += func(v)
            v = ""

        answer += ")"
        temp = ""
        for i in range(1,len(u)-1)  :
            if u[i] == "(":
                temp += ")"
            else :
                temp += "("
        answer += temp
    if v != "" :
        answer += func(v)
    return answer
def solution(p):
    
    return func(p)
