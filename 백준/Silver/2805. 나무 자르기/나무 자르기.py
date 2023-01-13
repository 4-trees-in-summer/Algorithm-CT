n, m = map(int, input().split())
data = list(map(int, input().split()))

max_d = max(data)

def binary_search(start, end) :
  if start > end :
    print(end)
    return end

  mid = (start+end)//2
  cnt = 0
  
  for i in data :
    if i >= mid :
      cnt += i - mid

  if cnt >= m :
    binary_search(mid+1, end)
  else :
    binary_search(start, mid-1)

binary_search(1, max_d)