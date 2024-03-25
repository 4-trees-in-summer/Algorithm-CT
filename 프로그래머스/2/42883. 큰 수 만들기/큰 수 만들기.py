def solution(number, k):
    answer = ''
    answer_l = len(number) - k
    stack = []
    for idx, num in enumerate(number) :
        if answer_l == len(answer) :
            break
        
        if not stack or stack[-1] >= num :
            stack.append(num)
            continue
        
        while stack and stack[-1] < num and k > 0 :
            stack.pop()
            k -= 1
        
        stack.append(num)
        
    return ''.join(stack[:answer_l])