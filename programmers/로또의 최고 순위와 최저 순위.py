#
def solution(lottos, win_nums):
    answer = []
    count =0
    count_zero = 0
    for lotto in lottos :
        if lotto in win_nums :
            count += 1
        elif lotto == 0:
            count_zero += 1

    if count+count_zero >= 2 :
        answer.append(7-(count+count_zero))
    else :
        answer.append(6)
        
    if count >= 2:
        answer.append(7-count)
    else :
        answer.append(6)

    return answer
