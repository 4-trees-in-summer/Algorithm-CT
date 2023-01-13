n1 = int(input())
A = list(map(int, input().split()))
n2 = int(input())
data = list(map(int, input().split()))

A.sort()

def binary_search (obj, start, end) :
  if start > end :
    return 0
    
  center = (start+end)//2

  if A[center] == obj :
    return 1
  elif A[center] > obj :
    return binary_search(obj, start, center-1)
  else :
    return binary_search(obj, center+1, end)

for i in data :
  start = 0
  end = len(A)-1
  
  print(binary_search(i, start, end))