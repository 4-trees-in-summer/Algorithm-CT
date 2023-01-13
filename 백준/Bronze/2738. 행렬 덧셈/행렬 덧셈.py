x, y = map(int, input().split())

array1 = []
array2 = []

row = []

for i in range(x):
  row = list(map(int, input().split()))  
  array1.append(row)

for i in range(x):
  row = list(map(int, input().split()))  
  array2.append(row)

for i in range(x):   
  for j in range(y):
    if i == x-1 and j == y-1:
      print(array1[i][j]+array2[i][j])
    else:
      print(array1[i][j]+array2[i][j], end = " ")
    
  print()