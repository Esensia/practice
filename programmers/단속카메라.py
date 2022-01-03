def solution(routes):

    answer = 0

    routes.sort(key=lambda x : (x[1],x[0])) # 끝나는 값이 작은 수부터 정렬

    n = -30001
    
    for i in range(0,len(routes)) :
        if n < routes[i][0] : # 구간 종료 지점이 다음 차량의 시작지점보다 작으면
            n = routes[i][1] # n에 다음 차량의 종료지점 저장
            answer += 1 # CCTV설치
    return answer
