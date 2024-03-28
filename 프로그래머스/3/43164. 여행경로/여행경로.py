import copy

def solution(tickets):
    answer = []
    stack = []
    
    tickets.sort(key = lambda x:(x[0], x[1]))
    answer_l = len(tickets) + 1
    airport = 'ICN'
    stack.append(airport)
    used_tickets = []
    visited_route = []
    
    while(1):
        airport = stack[-1]
        
        for idx, (departure, destination) in enumerate(tickets) :
            if departure == airport :
                stack.append(destination)
                
                stack_pop = False
                for route in visited_route :
                    if stack == route :
                        stack.pop()
                        stack_pop = True
                        break
                
                if stack_pop :
                    continue
                    
                used_tickets.append(tickets.pop(idx))
                break
        
        if len(stack) == answer_l :
            break
        
        if stack[-1] == airport :
            visited_route.append(copy.deepcopy(stack))
            stack.pop()
            tickets.append(used_tickets.pop())
        
        print("Answer:", stack)
        print("visited_route:", visited_route)
        
        print()
        
    return stack