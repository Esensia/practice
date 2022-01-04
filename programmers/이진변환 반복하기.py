def solution(s):
    answer = []
    zero_count = 0
    count = 0
    while len(s) != 1 :
        length = s.count("1")
        zero_count += len(s) - length
        
        s = format(length, "b")
        count += 1
    answer = [count, zero_count]
    return answer
