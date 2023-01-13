data = []

for i in range(5):
  x = int(input())
  data.append(x)

sum = 0
min = 100

for i in range(len(data)):
  sum+=data[i]

for i in range(3):
  for j in range(len(data)):
    if min > data[j] :
      min = data[j]
      index = j

  answer = data[index]
  data[index] = 101
  min = 101

print(int(sum/len(data)))
print(answer)
