def solution(s):
    answer = float('inf')

    if len(s) == 1:
        return 1

    for i in range(1,(len(s)//2)+1) :
        temp = s[:i]
        cnt = 1
        ans = 0
        for j in range(i,len(s),i) :
            if temp == s[j:j+i] :
                cnt += 1
            else :
                if cnt != 1 :
                    ans += len(temp) + len(str(cnt))
                else :
                    ans += len(temp)
                temp = s[j:j+i]
                cnt = 1
                
        if cnt != 1: 
            ans += len(temp) + len(str(cnt))
        else: 
            ans += len(temp)
        answer = min(answer,ans)
    
    return answer
