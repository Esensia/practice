import heapq

def solution(genres, plays):
    answer = []
    dic = {}
    
    for i in range(len(genres)) :
        if genres[i] in dic :
            dic[genres[i]] += plays[i] # 내가 왜 여기서 dic[genres[i]] + plays[i] 를 해서 자꾸 삽질했을까...
        else :
            dic[genres[i]] = plays[i]

    sum_dic = []
    for d in dic :
        sum_dic.append((d,dic[d]))
    sum_dic.sort(key=lambda x : (-x[1],x[0]))
    
    result = []
    for g in sum_dic :

        heap = []
        count = 0
        for i in range(len(genres)) :

            if g[0] == genres[i] :
                heap.append((i,plays[i]))
                
        heap.sort(key=lambda x : (-x[1],x[0]))
        while len(heap) != 0 :
            if count == 2 : 
                break
            count += 1
            result.append(heap.pop(0)[0])
        heap.clear()
    return result
