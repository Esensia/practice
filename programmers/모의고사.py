def solution(answers):
    answer = []
    nodap1 = []
    nodap2 = []
    nodap3 = []
    for i in range(2000):
        nodap1.extend([1,2,3,4,5])
    for i in range(1500):
        nodap2.extend([2,1,2,3,2,4,2,5])
    for i in range(1000):
        nodap3.extend([3,3,1,1,2,2,4,4,5,5])
    
    count = [0,0,0]
    for i in range(len(answers)) :
        if answers[i] == nodap1[i] :
            count[0] = count[0] + 1
        if answers[i] == nodap2[i] :
            count[1]+=1
        if answers[i] == nodap3[i] :
            count[2]+=1

    maxcount = max(count)
    
    for i in range(len(count)) :
        if maxcount == count[i] :
            answer.append(i+1)
    return answer
