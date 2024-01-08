def solution(phone_book):
    phone_book.sort()
    
    for idx in range(len(phone_book)-1) :
        s1 = phone_book[idx] 
        s2 = phone_book[idx+1]
        
        if s1 == s2[:len(s1)] :
            return False
    
    return True