from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())

s = []
for _ in range(N) :
    s.append(list(map(int, input().split())))

index = []
for i in range(N) :
    for j in range(M) :
        if s[i][j] == 0 :
            index.append((i,j))
            
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

combi = list(combinations(index, 3))

def bfs(combi) :
    q = deque()
    s_ = copy.deepcopy(s)
    for i in range(len(s_)) :
        for j in range(len(s_[0])) :
            if s_[i][j] == 2 :
                q.append((i,j))
            if (i,j) in combi :
                s_[i][j] = 1

    while q :
        r,c = q.popleft()

        for dir in directions :
            dr, dc = r-dir[0], c-dir[1]

            if (0 <= dr < N) and (0 <= dc < M) :
                if s_[dr][dc] == 0:
                    s_[dr][dc] = 2
                    q.append((dr,dc))

    global result
    temp = 0
    for i in s_ :
        temp += i.count(0)

    result = max(result, temp)


result = 0

for c in combi :
    bfs(c)

print(result)