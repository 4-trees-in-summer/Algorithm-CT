import heapq

def find_parent(parent, node) :
    if parent[node] != node :
        return find_parent(parent, parent[node])
    return node

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def solution(n, costs):
    answer = 0 
    
    parent = list(range(n+1))
    edges = []
    for i in costs :
        heapq.heappush(edges, [i[2], i[0], i[1]])
        
    while edges :
        cost, a, b = heapq.heappop(edges)
        
        if find_parent(parent, a) != find_parent(parent, b) :
            union_parent(parent, a, b)
            answer += cost
            
    return answer
        
        
        
        
        
        
        
        
        
    
    