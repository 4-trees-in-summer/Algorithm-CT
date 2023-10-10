# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.

from collections import deque

N = int(input())

maze = []
for _ in range(N) :
    temp = list(map(int, input().split()))
    maze.append(temp)

directions = [[-1,0], [0,-1], [1,0], [0,1]]

# def check_fish(shark) :
#     cnt = 0
#     idx = []
#     emergence = False
#     shark_index = [-1, -1]
#     for i in range(len(maze)) :
#         for j in range(len(maze[0])) :
#             if 0 < maze[i][j] < shark :
#                 cnt += 1
#             elif maze[i][j] == 9 :
#                 shark_index = [i,j]
#                 maze[i][j] = 0
#
#     if cnt == 0 :
#         return cnt, [-1, -1], emergence
#
#     emergence = bfs_check(shark_index[0], shark_index[1], shark)
#     return cnt, shark_index, emergence


# def bfs_check(shark_r, shark_c, shark) :
#     q = deque()
#     q.append([shark_r, shark_c, 0])
#     visited = []
#
#     while q:
#         shark_r, shark_c, dist = q.popleft()
#
#         dist += 1
#         for idx, dir in enumerate(directions):
#             shark_r_, shark_c_ = shark_r + dir[0], shark_c + dir[1]
#
#             if (0 <= shark_r_ < N) and (0 <= shark_c_ < N):
#                 # 똑같거나 0이면 지나가고
#                 if (maze[shark_r_][shark_c_] in (shark, 0)) and ([shark_r, shark_c] not in visited) :
#                     visited.append([shark_r_, shark_c_])
#                     q.append([shark_r_, shark_c_, dist])
#
#                 # 작으면 먹어야지
#                 elif maze[shark_r_][shark_c_] < shark:
#                     return False
#
#     return True

def bfs(shark_r, shark_c, shark, shark_eat) :
    q = deque()
    q.append([shark_r, shark_c, 0])

    first = True
    ans_dist = 1000000
    fish_list = []
    visited = [[shark_r, shark_c]]
    while q :
        shark_r, shark_c, dist = q.popleft()

        dist += 1
        if dist > ans_dist :
            break

        for idx, dir in enumerate(directions) :
            shark_r_, shark_c_ = shark_r+dir[0], shark_c+dir[1]

            if (0 <= shark_r_ < N) and (0 <= shark_c_ < N) and ([shark_r_, shark_c_] not in visited):
                # 똑같거나 0이면 지나가고
                if (maze[shark_r_][shark_c_] in (shark, 0))  :
                    q.append([shark_r_, shark_c_, dist])
                    visited.append([shark_r_, shark_c_])
                # 작으면 먹어야지
                elif maze[shark_r_][shark_c_] < shark :
                    if first :
                        ans_dist = dist
                        first = False

                    fish_list.append([shark_r_, shark_c_, dist])
    if fish_list :
        fish_list.sort(key = lambda x : (x[0], x[1]))

        maze[fish_list[0][0]][fish_list[0][1]] = 0
        shark_eat += 1
        if shark == shark_eat :
            shark += 1
            shark_eat = 0

        return fish_list[0][0], fish_list[0][1], shark, shark_eat, fish_list[0][2]

    else :
        return -1, -1, -1, -1, 0


shark = 2
answer = 0
shark_eat = 0

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 9:
            shark_r, shark_c = i, j
            maze[i][j] = 0
            break

while True :
    # fish_cnt, shark_index_, emergence = check_fish(shark)
    # # print(fish_cnt, shark_index_, emergence)
    # # print(shark)
    shark_r, shark_c, shark, shark_eat, dist = bfs(shark_r, shark_c, shark, shark_eat)

    answer += dist
    # print(shark_r, shark_c, answer)
    if dist == 0 :
        # for i in maze :
            # print(i)
        print(answer)
        break
