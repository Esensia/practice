def solution(n, t, m, timetable):
    answer = 0
    second = []

    for time in timetable :
        hm = time.split(":")
        h = hm[0]
        mm = hm[1]
        second.append(int(h) * 60 + int(mm))
    second.sort()
    shuttle_time = 540
    idx = 0
    for i in range(1,n+1):
        if i > 1:
            shuttle_time += t
        people = 0 
    
        for j in range(idx,len(second)) :
            if second[j] <= shuttle_time :
                idx += 1
                people += 1
                if people == m :
                    break
        if i == n :
            if people == m :
                answer = second[idx-1] -1
            else :
                answer = shuttle_time
    
    answer = str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
    return answer
