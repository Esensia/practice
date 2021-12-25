import bisect

def solution(N, stages):
    answer = []
    stages.sort()
    length = len(stages)
    for i in range(1,N+1):
        if length == 0 :
            answer.append((i,0))
            continue
        
        lower_bound = bisect.bisect_left(stages, i)
        upper_bound = bisect.bisect_right(stages, i)
        
        people = upper_bound - lower_bound
           
        answer.append((i,people/length))
        length -= people
        
    answer.sort(key=lambda x : (-x[1],x[0]))
    result = []
    for ans in answer :
        result.append(ans[0])
    return result
