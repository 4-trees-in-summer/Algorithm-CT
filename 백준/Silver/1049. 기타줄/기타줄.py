N, M = list(map(int, input().split()))

brand = []
brand_6 = 1001
brand_1 = 1001
for i in range(M):
    brand = list(map(int, input().split()))

    temp = min(brand[0], brand[1]*6)
    if brand_6 > temp :
        brand_6 = temp

    if brand_1 > brand[1] :
        brand_1 = brand[1]

if brand_6 < brand_1*6 :
    if brand_6 <= (N%6)*brand_1 :
        print((N//6 + 1)*brand_6)
    else :
        print((N//6)*brand_6 + (N%6)*brand_1)
        
elif brand_6 >= brand_1*6 :
    print((N//6)*brand_6 + (N%6)*brand_1)
