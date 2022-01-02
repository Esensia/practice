def solution(people, limit):
    answer = 0
    people.sort(key=lambda x : -x)
    start = 0
    end = len(people) -1
    
    while start < end :
        sum_num = people[start] + people[end]
        if sum_num > limit :
            start += 1
        else :
            start += 1
            end -= 1
        answer += 1
    if start == end :
        answer += 1
    return answer
