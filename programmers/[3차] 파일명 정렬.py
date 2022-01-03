def solution(files):
    answer = []
    new_file = []
    count = 0
    for file in files :
        
        idx = 0
        head = ""
        number = ""
        tail = ""
        for i in range(len(file)) :
            if file[i].isdigit() :
                if idx == 0 :
                    head = file[:i]
                    idx = i
            elif idx != 0 and not file[i].isdigit() :
                number = file[len(head):i]
                tail = file[i:]
                break
        if number == "":
            number = file[idx:]
        new_file.append((head,number,tail,count,int(number)))
        count+=1

    new_file.sort(key = lambda x : (x[0].lower(),x[4],x[3]))
    
    for file in new_file :
        string = file[0]+file[1]+file[2]
        answer.append(string)
    return answer
