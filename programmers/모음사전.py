# 완탐도 되지만 수열의 특징을 통해 계차수열임을 알 수 있다.
def solution(word):
    dic = {"A":1,"E":2,"I":3,"O":4,"U":5}

    sum = 0
    for i in range(len(word)) :
        gyecha = 0
        for s in range(5-i) :
            gyecha += pow(5,s)
        sum += gyecha * (dic[word[i]] -1)
    answer = sum + len(word)
    return answer
