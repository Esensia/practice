def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for i in range(n+1)] #이중리스트를 선언할 때 안에 for로 해야한다.. [[0] * m] * n 으로 하면 각각의 행들이 같은 객체로 인식된다..
    
    for puddle in puddles :
        dp[puddle[1]][puddle[0]] = -1
    dp[1][1]=1
    for y in range(1,n+1) :
        for x in range(1,m+1) :
            if y == 1 and x == 1:
                continue
            if dp[y][x] == -1:
                continue
            if dp[y-1][x] != -1 and dp[y][x-1] != -1:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
            elif dp[y-1][x] == -1 :
                dp[y][x] = dp[y][x-1]
            elif dp[y][x-1] == -1 :
                dp[y][x] = dp[y-1][x]
    
    answer = dp[n][m]%1000000007

    return answer
