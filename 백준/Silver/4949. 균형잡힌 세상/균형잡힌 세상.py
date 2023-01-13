while True :
  s = input()
  stack = []

  check = 0
  
  if s == '.' :
    break

  for i in s:
    if i == '[' or i == '(' :
      stack.append(i)
      
    elif i == ']' :
      if len(stack) == 0 :
        check = 1
        break        
      elif stack[-1] == '[' :
        stack.pop()
      else :
        check = 1
        break
        
    elif i == ')' :
      if len(stack) == 0:
        check = 1
        break
      elif stack[-1] == '(' :
        stack.pop()
      else :
        check = 1
        break
        
  if len(stack) == 0 and check == 0 :
    print('yes')
  else :
    print('no')