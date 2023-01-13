s = input()
alpha = "ABC DEF GHI JKL MNO PQRS TUV WXYZ"
alpha = list(alpha.split())

cnt = 0

for i in s :
  for j in range(8) :
    if i in alpha[j] :
      cnt += j+3

print(cnt)      