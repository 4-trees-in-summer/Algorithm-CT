n = int(input())

data = list(map(int, input().split()))

count = 0
for i in data :
  cnt = 0
  if i == 1 :
    continue
    
  for j in range(1, i+1) :
    if i%j == 0 :
      cnt += 1

  if cnt == 2 :
    count += 1

print(count)
