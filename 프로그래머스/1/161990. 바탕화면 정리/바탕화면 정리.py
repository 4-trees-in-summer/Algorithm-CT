def distance(r1, c1, r2, c2) :
    return abs(r1-r2) + abs(c1-c2)
    
def solution(wallpaper):
    answer = []
    
    smallest_r = len(wallpaper)
    smallest_c = len(wallpaper[0])
    
    
    for r, line in enumerate(wallpaper) :
        for c, dot in enumerate(line) :
            if dot == '#' :
                answer.append([r,c])
    
    sorted_for_r = sorted(answer, key = lambda x:x[0])
    sorted_for_c = sorted(answer, key = lambda x:x[1])
    
    upper_r = sorted_for_r[0][0]
    upper_c = sorted_for_c[0][1]
    
    down_r = sorted_for_r[-1][0]
    down_c = sorted_for_c[-1][1]
    
    return [upper_r, upper_c, down_r+1, down_c+1]