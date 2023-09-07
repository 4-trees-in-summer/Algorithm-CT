from itertools import zip_longest

def solution(str1, str2):
    answer = 0
    
    def make_list(str_) :
        temp = []
        for idx in range(len(str_)-1) :
            s1, s2 = str_[idx], str_[idx+1]
            
            if s1.isalpha() and s2.isalpha() :
                s = s1.lower()+ s2.lower()
                temp.append(s)
        
        return temp
            
    str_list_1 = make_list(str1)
    str_list_2 = make_list(str2)
    
    gyo = 0
    repeat = []
    for s1 in str_list_1 :
        for idx, s2 in enumerate(str_list_2) :
            if s1 == s2 and idx not in repeat :
                gyo += 1
                repeat.append(idx)
                break

    hap = len(str_list_1) + len(str_list_2) -gyo
    print(gyo, hap)
    if hap == 0 :
        return 65536
    else :
        return int(gyo/hap*65536)