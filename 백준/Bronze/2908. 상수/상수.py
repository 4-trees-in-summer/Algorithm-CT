x, y = input().split()

rev_x = int(x[::-1])
rev_y = int(y[::-1])

if rev_x > rev_y :
  print(rev_x)
else :
  print(rev_y)