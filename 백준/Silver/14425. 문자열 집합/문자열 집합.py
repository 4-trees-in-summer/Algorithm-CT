n, k = map(int, input().split())

word = []
count = 0

for i in range(n) :
  word.append(input())

word.sort()

for j in range(k) :
  x = input()

  start = 0
  end = len(word) - 1

  while start <= end :
    mid = (end + start)//2
    
    if x > word[mid] :
      start = mid + 1
    elif x < word[mid] :
      end = mid - 1
    else :
      count += 1
      break

print(count)
