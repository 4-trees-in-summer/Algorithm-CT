x = input()

count = 0 

for i in range(len(x)):
  if x[i] == ' ':
    count+=1
    
if x[0] == ' ':
  count-=1
if x[len(x)-1] == ' ':
  count-=1    

print(count+1)