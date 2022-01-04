import copy
ans = []
def solution(tickets):
    answer = ["ICN"]
    airport = "ICN"
    dic = {}
    
    for ticket in tickets :
        dep = ticket[0]
        des = ticket[1]
        if dep not in dic :
            dic[dep] = [des]
        else :
            dic[dep].append(des)
    for d in dic:
        dic[d].sort()
    
    def dfs(city,count) :
        
        global ans
        
        if count == len(tickets) :
            temp = copy.deepcopy(answer)
            ans.append(temp)
            return
        if city not in dic : # 여기땜에 자꾸 오류났었음.. dict의 경우 key에 해당하는 value 처리를 해줬어야함.. [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]] 인 경우 A : key error
            return
        city_list = dic[city]

        if len(city_list) == 0:
            return
        for airport in city_list :
            
            dic[city].remove(airport)
            answer.append(airport)
            dfs(airport, count+1)
            answer.pop()
            dic[city].append(airport)
            dic[city].sort()
    dfs("ICN",0)
    
    return ans[0]
