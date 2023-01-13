n = int(input())
card = list(range(1, n+1))

k = 0
cnt = 0
i = 0

while True :
  if cnt == n-1 :
    print(card[-1])
    break

  elif k%2 == 0 :
    cnt += 1
    k += 1
  elif k%2 == 1 :
    card.append(card[k])
    k += 1