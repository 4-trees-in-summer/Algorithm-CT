cnt = int(input())

for i in range(cnt):
  k = input().split()

  for j in k[1]:
    for i in range(int(k[0])) :
      print(j, end = "")
    
  print()