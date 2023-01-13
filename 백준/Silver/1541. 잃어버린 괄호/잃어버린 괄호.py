ex = input().split('-')
real_sum = []

for i in ex :
  sum = 0
  i = i.split('+')

  for j in i :
    sum += int(j)

  real_sum.append(sum)

answer = real_sum[0]

for i in range(1, len(real_sum)):
  answer -= real_sum[i] 

print(answer)