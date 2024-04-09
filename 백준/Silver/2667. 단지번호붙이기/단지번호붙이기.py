N = int(input())
answer_list = []
_map = []
for _ in range(N) :
    _map.append(list(map(int, list(input()))))

visited = [[False for _ in range(N)] for _ in range(N)]

d_r = [0, 0, 1, -1]
d_c = [1, -1, 0, 0]

def dfs(r,c) :
    global visited

    if visited[r][c] or _map[r][c] == 0 :
        return

    stack =[[r,c]]
    cnt = 1
    while stack :
        r,c = stack[-1]
        visited[r][c] = True
        for direction in range(4) :
            r_ = r + d_r[direction]
            c_ = c + d_c[direction]
            if not((0 <= r_ < N) and (0 <= c_ < N)) :
                continue

            if visited[r_][c_] or _map[r_][c_] == 0 :
                continue

            stack.append([r_, c_])
            cnt += 1
            break
        else :
            stack.pop()

    return cnt

for r in range(N) :
    for c in range(N) :
        answer = dfs(r,c)
        if answer :
            answer_list.append(answer)

print(len(answer_list))
for answer in sorted(answer_list) :
    print(answer)