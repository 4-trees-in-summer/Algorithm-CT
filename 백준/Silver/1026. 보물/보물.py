answer = 0 

l = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = sorted(A)
B_sorted = sorted(B, reverse=True)

for i in range(l) :
  answer += A_sorted[i]*B_sorted[i]

print(answer)