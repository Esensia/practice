def solution(cacheSize, cities):
    answer = 0
    cache = [0 for i in range(cacheSize)]
    time = 0
    if cacheSize == 0 :
        return len(cities) * 5
    for citi in cities :
        citi = citi.lower()
        if citi in cache :
            cache.remove(citi)
            cache.append(citi)
            time += 1
        elif len(cache) < cacheSize :
            cache.append(citi)
            time += 5
        elif len(cache) == cacheSize :
            cache.pop(0)
            cache.append(citi)
            time += 5
    answer = time
    return answer
