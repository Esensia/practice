def solution(brown, yellow):
    answer = []
    i = 1
    while True :
        if yellow == i * ((brown/2 -i)-2) :
            answer.append((brown/2 -i))
            answer.append(i+2)
            break
        i+=1
        
    return answer
