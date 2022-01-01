def solution(citations):
    answer = 0
    citations.sort()
    max_ci =0
    for h in range(1,len(citations)+1) :
        for i in range(len(citations)) :
            if citations[i] >= h and len(citations) - i >= h and i+1 <= h : max_ci = h
            
    return max_ci
