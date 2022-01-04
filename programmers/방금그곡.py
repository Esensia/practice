def solution(m, musicinfos):
    answer = []
    temp_m = ""
    idx = 0
    while idx < len(m) :
        if idx < len(m)-1 and  m[idx] == "C" and m[idx+1] == "#" :
            temp_m += "1"
            idx+=1
        elif idx < len(m)-1 and  m[idx] == "D" and m[idx+1] == "#" :
            temp_m += "2"
            idx+=1
        elif idx < len(m)-1 and  m[idx] == "F" and m[idx+1] == "#" :
            temp_m += "3"
            idx+=1
        elif idx < len(m)-1 and  m[idx] == "G" and m[idx+1] == "#" :
            temp_m += "4"
            idx+=1
        elif idx < len(m)-1 and  m[idx] == "A" and m[idx+1] == "#" :
            temp_m += "5"
            idx+=1
        else :
            temp_m += m[idx]
        idx +=1
    m = temp_m
    count = 0
    for musicinfo in musicinfos :
        music_list = musicinfo.split(",")
        
        start = int(music_list[0].split(":")[0]) * 60 + int(music_list[0].split(":")[1])
        end = int(music_list[1].split(":")[0]) * 60 + int(music_list[1].split(":")[1])
        music = music_list[2]
        melody = music_list[3]
        idx = 0
        temp = ""
        while idx < len(melody) :
            if idx < len(melody)-1 and  melody[idx] == "C" and melody[idx+1] == "#" :
                temp += "1"
                idx+=1
            elif idx < len(melody)-1 and  melody[idx] == "D" and melody[idx+1] == "#" :
                temp += "2"
                idx+=1
            elif idx < len(melody)-1 and  melody[idx] == "F" and melody[idx+1] == "#" :
                temp += "3"
                idx+=1
            elif idx < len(melody)-1 and  melody[idx] == "G" and melody[idx+1] == "#" :
                temp += "4"
                idx+=1
            elif idx < len(melody)-1 and  melody[idx] == "A" and melody[idx+1] == "#" :
                temp += "5"
                idx+=1
            else :
                temp += melody[idx]
            idx +=1
            
        playtime = end - start
        melody_str = ""
        while len(melody_str) <= 1440 :
            melody_str += temp
        melody_str = melody_str[:playtime]
        
        if m in melody_str :
            answer.append([music,playtime,count])
        count+=1
    
    if len(answer) == 0:
        return "(None)"
    answer.sort(key=lambda x : (-x[1],x[2]))
    return answer[0][0]
