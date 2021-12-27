import heapq

def solution(jobs):
    answer = 0
    heap = []
    heapq.heapify(heap)
    length = len(jobs)
    i = 0
    time = 0
    
    jobs.sort(key=lambda x : x[0])

    while len(jobs) > i or len(heap) !=0:
        if len(jobs) > i and time >= jobs[i][0] :
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]) )
            i+=1
            continue
        if len(heap) != 0 :
            time += heap[0][0]
            answer += time - heap[0][1]
            heapq.heappop(heap)
        else :
            time = jobs[i][0]
    return answer//length
