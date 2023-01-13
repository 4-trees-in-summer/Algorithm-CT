n = int(input())
n_list = list(map(int, input().split()))
k = int(input())

cnt = 0

for i in n_list:
  if i == k :
    cnt+=1
    
print(cnt)