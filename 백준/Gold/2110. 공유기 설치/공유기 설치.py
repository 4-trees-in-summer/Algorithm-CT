n, k = map(int, input().split())
data = []

for i in range(n) :
  data.append(int(input()))
data.sort()

def binary_search(start, end) :
  if start > end :
    return start-1

  mid = (start+end)//2
  temp = data[0]

  cnt = 1
  for i in data :
    if i-temp >= mid :
      temp = i
      cnt += 1

  if cnt >= k :
    return binary_search(mid+1, end)
  else :
    return binary_search(start, mid-1)

print(binary_search(1, data[-1]-data[0]))