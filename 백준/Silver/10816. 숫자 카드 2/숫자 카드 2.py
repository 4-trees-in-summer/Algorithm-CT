import sys

n1 = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))

n2 = sys.stdin.readline()
check = list(map(int, sys.stdin.readline().split()))

card.sort()

count = {}

j = 1

for i in range(len(card)-1) :
  if card[i] != card[i+1] :
    if i == (len(card)-2):
      count[card[i]] = j
      count[card[i+1]] = 1
    else:
      count[card[i]] = j
      j = 1
  
  elif  card[i] == card[i+1] :
    if i == (len(card)-2):
      j+=1
      count[card[i]] = j  
    else:
      j += 1

for i in check :
  if i in count :
    print(count[i], end = ' ')
  else:
    print(0, end = ' ')