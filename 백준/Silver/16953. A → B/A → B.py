a, b = list(map(int, input().split()))
cnt = 1

while a < b :
    cnt += 1
    if b%10 == 1 :
        b //= 10
    elif b%2 == 0 :
        b //= 2
    else :
        b = -1

    if b == a :
        print(cnt)
        break

else :
    print(-1)