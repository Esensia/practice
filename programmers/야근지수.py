import heapq
def solution(n, works):
    answer = 0
    
    heap = []
    heapq.heapify(heap)
    
    for work in works :
        heapq.heappush(heap,-work)
    
    while n > 0 and len(heap) > 0:
        work = -heapq.heappop(heap)
        if work > 1 :
            heapq.heappush(heap,-(work-1))
        n -= 1
    
    if len(heap) == 0 :
        answer = 0
    else :
        work_sum = 0
        while len(heap) > 0 :
            work_sum += (heapq.heappop(heap)**2)
        answer = work_sum
    return answer
