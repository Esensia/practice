def solution(progresses, speeds):
    answer = []
    
    new_progresses = []
    for i in range(len(progresses)) :
        remain = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] > 0 :
            remain += 1
        new_progresses.append((progresses[i],remain ))

    print(new_progresses)
    release = new_progresses[0][1]
    count = 1
    for i in range(len(new_progresses)) :
        if i == 0 : continue
        if new_progresses[i][1] > release:
            
            release = new_progresses[i][1]
            answer.append(count)
            count = 1
        else :
            count+=1
        if i == len(new_progresses)-1 :
            if release == new_progresses[i][1] :
                answer.append(count)
    if count > 1:
        answer.append(count)

    return answer
