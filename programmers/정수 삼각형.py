def solution(triangle):
    answer = 0
    dp = [[0] * len(triangle)] * len(triangle)

    for y in range(len(triangle)-1,-1,-1):
        for x in range(len(triangle[y])) :
            if y == len(triangle)-1 :
                dp[y][x] = triangle[y][x]
                
            else :
                dp[y][x] = max(dp[y][x],dp[y][x+1]) + triangle[y][x]
    answer = max(dp[0])
    
    return answer
