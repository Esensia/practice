def solution(new_id):
    answer = ""
    temp_id1 = new_id.lower()
    temp_id2 = ""
    for s in temp_id1 :
        if s.isdigit() :
            temp_id2 += s
        elif s.islower() :
            temp_id2 += s
        elif s == "-" or s == "_" or s =="." :
            temp_id2 += s

    temp_id3 = ""
    for i in range(len(temp_id2)) :
        if len(temp_id3) == 0 :
            temp_id3 +=temp_id2[i]
            continue
            
        if temp_id2[i] == "." and temp_id3[-1] == "." :
            continue
        temp_id3 +=temp_id2[i]
    temp_id4 = temp_id3
    if temp_id3[0]==".":
        temp_id4 = temp_id4[1:]
    if temp_id3[-1] == ".":
        temp_id4 = temp_id4[:-1] 
    
    temp_id5 = temp_id4

    if len(temp_id5) == 0:
        temp_id5 ="a"
        
    temp_id6 = temp_id5
    if len(temp_id5) >= 16 :
        temp_id6 = temp_id5[:15]
    
    print(temp_id6)
    
    if temp_id6[-1] == ".":
        temp_id6 = temp_id6[:-1]
    
    if len(temp_id6) <= 2:
        while len(temp_id6) != 3:
            temp_id6 += temp_id6[-1]
    answer = temp_id6
    
    return answer
