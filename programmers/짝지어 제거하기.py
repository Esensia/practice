def solution(s):
    
    stack = []
    
    for ch in s :
        if len(stack) == 0 or stack[-1] != ch:
            stack.append(ch)
        elif stack[-1] == ch :
            stack.pop()
    if len(stack) == 0:
        answer = 1
    else :
        answer = 0
            
    return answer
