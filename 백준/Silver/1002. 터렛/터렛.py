import math

cnt = int(input())
case = []

for i in range(cnt) :
  case.append(list(map(int ,input().split())))

for i in range(cnt) :
  dist = math.sqrt((case[i][0]-case[i][3])**2 + (case[i][1]-case[i][4])**2)
  if dist == 0 :
    if case[i][2] == case[i][5] :
      print(-1)
      continue 
    else :
      print(0)
      continue
      
  if dist < case[i][2] + case[i][5] :
    if dist+min(case[i][2],case[i][5]) < max(case[i][2], case[i][5]) :
      print(0)
    elif dist+min(case[i][2],case[i][5]) == max(case[i][2], case[i][5]) :
      print(1)
    else :
      print(2)
  elif dist == case[i][2] + case[i][5] :
    print(1)
  else :
    print(0)