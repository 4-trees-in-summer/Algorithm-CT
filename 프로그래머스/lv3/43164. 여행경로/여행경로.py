from collections import defaultdict

def solution(tickets):
    path = [] 
    
    tickets.sort(key = lambda x:x[1], reverse=True)
    
    graph = defaultdict(list)
    for start, end in tickets :
        graph[start].append(end)
        
    stack = ['ICN']
    
    while stack :
        airport = stack.pop()
        
        if airport not in graph or not graph[airport] :
            path.append(airport)
        else :
            stack.append(airport)
            stack.append(graph[airport].pop())
    
    
    return path[::-1]