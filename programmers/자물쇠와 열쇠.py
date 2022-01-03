from copy import deepcopy

def solution(key, lock):
    answer = False
    size = len(lock)
    
    for c in range(4) :
        temp = deepcopy(key)
        for j in range(len(key)) :
            for k in range(len(key[j])) :
                key[j][k] = temp[len(key)-1-k][j] # 90도 회전
        
        for row in range(-size+1, size) :
            for col in range(-size+1, size):
                
                flag = True
                for i in range(size) :
                    for j in range(size) :
                        if row+i < 0 or row+i >= len(key) or col+j < 0 or col+j >= len(key) :
                            if lock[i][j] != 1:
                                flag = False
                                break
                        else :
                            if lock[i][j] + key[row+i][col+j] != 1:
                                flag = False
                                break
                    if flag == False:
                        break
                if flag :
                    answer = True
                    return answer
    return answer
