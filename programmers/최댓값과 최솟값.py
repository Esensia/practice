def solution(s):
    answer = ''
    list_num = list(map(int,s.split(" ")))
    
    list_num.sort()
    
    answer += str(list_num[0]) + ' '
    answer += str(list_num[-1])
    
    return answer
