word = list(input().upper())
visited = ([False]*len(word))
cnt = []
answer = []
  
for i in word :
  if visited[word.index(i)] :
    continue
  else :
    visited[word.index(i)] = True
  
  count = 0  
  for j in range(len(word)) :
    if i == word[j] and not visited[j] :
      count += 1
      visited[j] = True
      

  cnt.append(count)
  answer.append(i)

maxi = max(cnt)
max_index = cnt.index(max(cnt))
cnt.pop(max_index)

if maxi in cnt :
  print('?')
else:
  print(answer[max_index])