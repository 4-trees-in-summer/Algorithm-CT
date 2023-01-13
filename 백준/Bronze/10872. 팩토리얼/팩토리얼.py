n = int(input())

def pib(n) :
  if n == 1 or n == 0 :
    return 1
  else :
    return n*pib(n-1)

print(pib(n))