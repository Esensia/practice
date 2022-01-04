def solution(dirs):
    y = 5
    x = 5 
    dic = {}
    for dir in dirs :
        if dir == "U" :
            if y -1 >= 0 :
                dic[str(y) + str(x) + str(y-1) + str(x)] = "1"
                dic[str(y-1) + str(x) + str(y) + str(x)] = "1"
                y -=1
        elif dir == "L" :
            if x -1 >= 0 :
                dic[str(y) + str(x-1) + str(y) + str(x)] = "1"
                dic[str(y) + str(x) + str(y) + str(x-1)] = "1"
                x -=1
        elif dir == "R" :
            if x +1 <= 10 :
                dic[str(y) + str(x+1) + str(y) + str(x)] = "1"
                dic[str(y) + str(x) + str(y) + str(x+1)] = "1"
                x +=1
        elif dir == "D" :
            if y+1 <= 10 :
                dic[str(y+1) + str(x) + str(y) + str(x)] = "1"
                dic[str(y) + str(x) + str(y+1) + str(x)] = "1"
                y +=1

    return len(dic)//2
