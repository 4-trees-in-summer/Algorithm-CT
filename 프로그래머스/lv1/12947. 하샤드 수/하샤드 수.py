def solution(x):
    x_ = str(x)
    x_l = list(x_)
    
    if x%sum(list(map(int, x_l))) == 0 :
        return True
    else :
        return False