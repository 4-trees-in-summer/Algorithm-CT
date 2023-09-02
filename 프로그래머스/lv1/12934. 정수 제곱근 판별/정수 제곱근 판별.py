def solution(n):
    route_n = n**(1/2)
    if int(route_n) == route_n :
        return (route_n+1)**2
    else :
        return -1