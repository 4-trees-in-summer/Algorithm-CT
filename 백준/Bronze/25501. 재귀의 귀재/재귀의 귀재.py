import sys

def recursion(s, l, r, cnt) :
  if l >= r :
    return 1, cnt+1
  elif s[l] != s[r] :
    return 0, cnt+1
  else :
    return recursion(s,l+1, r-1, cnt+1)
  
def isPelindrome(s) :
  return recursion(s, 0, len(s)-1, 0)



n = int(input())

for i in range(n) :
  data = input()

  print(isPelindrome(data)[0], isPelindrome(data)[1] )