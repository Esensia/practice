def solution(number, k):
    answer = []
    number_list = list(number)
    
    for number in number_list :

        if len(answer) == 0 :
            answer.append(number)
            continue
        if k > 0:
            while answer[-1] < number:
                answer.pop()
                k -= 1
                if len(answer)==0 or k <= 0:
                    break
        answer.append(number)
    
    if k > 0 :
        answer = answer[:-k] # k가 남아있으면 숫자가 순서대로 들어왔으므로 마지막부터 k개를 지운다.

    return ''.join(answer)
