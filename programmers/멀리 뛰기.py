def solution(n):
    answer = 0
    
    dp = [0 for i in range(n+1)]
    
    if n >=3 :
        
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(3,n+1) :
            dp[i] = dp[i-1] + dp[i-2]
        answer = dp[n]%1234567
    elif n==1 :
        return 1
    else :
        return 2
    return answer
