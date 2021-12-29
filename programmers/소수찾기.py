import math
number_list = []

visited = [False] * 7
set_number = set()

def dfs(numbers) :

    if len(number_list) != 0 :
        set_number.add(int(''.join(number_list)))

    for i in range(len(numbers)) :

        if visited[i] == False :
            number_list.append(numbers[i])
            visited[i] = True
            dfs(numbers)
            visited[i] = False
            number_list.pop() #number_list.pop(0) 해놓고 계속 삽질만

def isPrime(n) :
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n%i ==0 :
            return False
    return True

def solution(numbers):
    answer = 0
    dfs(numbers)
    for num in set_number :
        if isPrime(num) :
            answer+=1
    return answer
