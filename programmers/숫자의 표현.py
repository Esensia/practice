def solution(n):
    answer = 0
    num_list = [i for i in range(1,n+1)]

    for i in range(0,n) :
        num_sum = 0
        m = i
        while num_sum < n and m < n :
            num_sum += num_list[m]
            m+=1
        if num_sum == n :
            answer += 1
        
    return answer
