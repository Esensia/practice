def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i in range(len(prices)) :
        price = prices[i]
        if len(stack) == 0 :
            stack.append((i,price))
        elif stack[-1][1] <= price:
            stack.append((i,price))
        else : 
            while True:
                if len(stack) == 0 or stack[-1][1] <= price :
                    stack.append((i,price))
                    break
                temp = stack.pop()
                answer[temp[0]] = i - temp[0] 
    while len(stack) >0 :
        temp = stack.pop()
        answer[temp[0]] = len(prices)-1 - temp[0] 
    return answer
