def solution(phone_book):
    
    dic = {}
    
    for str in phone_book:
        dic[str] = 1
    
    for str in phone_book:
        temp = ''
        for s in str :
            temp += s
            if temp in dic and temp != str:
                return False
    return True
