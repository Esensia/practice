# 안되는 상황들 모두 체크하기
def solution(places):
    answer = []
    
    for place in places :
        ans = -1
        for i in range(len(place)):
            if ans != -1:
                break
            for j in range(len(place)):
                if ans != -1:
                    break
                if place[i][j] == "P":
                    if (i + 1 < 5 and place[i+1][j] == "P") or (j + 1 < 5 and place[i][j+1] == "P"):
                        ans = 0
                        break
                    if (i + 2 < 5 and place[i+1][j] == "O" and place[i+2][j] =="P") or (j +2 < 5 and place[i][j+1] == "O" and place[i][j+2] == "P"):
                        ans = 0
                        break
                    if i+1<5 and j+1<5 and place[i+1][j+1]=="P" and not(place[i+1][j]=="X" and place[i][j+1]=="X") :
                        ans = 0
                        break
                    if i-1>=0 and j+1<5 and place[i-1][j+1]=="P" and not(place[i-1][j]=="X" and place[i][j+1]=="X") :
                        ans = 0
                        break
        if ans == -1:
            answer.append(1)
        else :
            answer.append(0)
        
    return answer
