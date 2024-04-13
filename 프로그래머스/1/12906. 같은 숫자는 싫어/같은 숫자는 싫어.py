def solution(arr):
    answer = []
    
    stack = [arr[0]]
    for a in arr[1:] :
        if a == stack[-1] :
            continue
        
        stack.append(a)
        

    return stack