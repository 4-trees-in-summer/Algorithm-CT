import sys

n, k = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for i in range(n)]

min_d = max(data)

def count(d) :
  cnt = 0
  
  for i in data :
    cnt += i//d    

  return cnt

def binary_search (start, end) :
  if start > end :
    return end

  mid = (start+end)//2
      
  if count(mid) >= k :
    return binary_search(mid+1, end)
    
  else :
    return binary_search(start, mid-1)

print(binary_search(1,min_d))