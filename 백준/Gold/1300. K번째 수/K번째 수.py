n = int(input())
k = int(input())

def search(start, end) :
  if start > end :
    return start

  mid = (start+end)//2

  cnt = 0
  for i in range(1, n+1) :
    cnt+=min(mid//i, n)

  if cnt >= k :
    return search(start, mid-1)
  else :
    return search(mid+1, end)

print(search(0, n*n))