x = input()

data = set()

for i in range(len(x)) :
  j = 1
  
  while i+j <= len(x) :
    data.add(str(x[i:i+j]))
    j += 1

print(len(data))