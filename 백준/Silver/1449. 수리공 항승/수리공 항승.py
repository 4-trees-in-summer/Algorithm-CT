n, l = list(map(int, input().split()))
water = list(map(int, input().split()))
water.sort()

def tape(n, l, water) :
    cnt = 0
    t = 0
    if l == 1 :
        return len(water)

    for w in water :
        if w > t :
            t = w+l-1
            cnt += 1

    return cnt

print(tape(n, l, water))