import math

def makeset(str) :
    result = []
    for i in range(len(str)-1) :
        head = str[i]
        tail = str[i+1]
        if head.isalpha() and tail.isalpha() :
            result.append(head.lower()+tail.lower())
    return result
def solution(str1, str2):
    answer = 0
    
    jaca_str1 = makeset(str1)
    jaca_str2 = makeset(str2)
    
    set1 = set(jaca_str1)
    set2 = set(jaca_str2)
    
    dic1 = {}
    dic2 = {}
    
    for s1 in set1 :
        dic1[s1] = 0
        for s2 in jaca_str2 :
            if s1 == s2 :
                dic1[s1] = dic1[s1]+1
                
    for s2 in set2 :
        dic2[s2] = 0
        for s1 in jaca_str1 :
            if s2 == s1 :
                dic2[s2] = dic2[s2]+1
    for s1 in dic1 :
        if dic1[s1] == 0 :
            dic1[s1] = jaca_str1.count(s1)
            
    for s2 in dic2 :
        if dic2[s2] == 0 :
            dic2[s2] = jaca_str2.count(s2)
    
    print(dic1)
    print(dic2)
    disjoint = 0
    union = 0
    
    for s1 in dic1 :
        if s1 in dic2 :
            disjoint += min(dic1[s1],dic2[s1])
            union += max(dic1[s1],dic2[s1])
        else :
            union += dic1[s1]
    
    for s2 in dic2 :
        if s2 not in dic1 :
            union += dic2[s2]
    if union == 0 and disjoint == 0:
        return 65536
    return math.trunc(disjoint/union * 65536)
