import sys

def binary_search (num, k, start, end) :
  while start <= end :
    mid = (start+end)//2
    
    if num[mid] < k :
      start = mid + 1
    elif num[mid] > k :
      end = mid - 1
    else :
      return True

  return False  
  
n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

cards.sort()

for i in checks :
  if binary_search(cards, i, 0, n-1) :
    print(1, end = ' ')
  else :
    print(0, end = ' ')