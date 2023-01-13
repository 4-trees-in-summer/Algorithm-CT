array = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
  if i in array:
    print(array.index(i), end = " ")
  else:
    print(-1, end = " ")