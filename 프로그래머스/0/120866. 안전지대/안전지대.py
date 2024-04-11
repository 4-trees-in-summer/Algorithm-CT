from copy import deepcopy

def solution(board):
    answer = 0
    # bomb_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    bomb_board = deepcopy(board)
    
    d_r = [1, 1, 1, 0, 0, -1, -1 ,-1, 0]
    d_c = [1, 0, -1, 1, -1, 1, 0, -1, 0]
    for r in range(len(board)) :
        for c in range(len(board[0])) :
            if board[r][c] == 0 :
                continue
                
            for d_r_, d_c_ in zip(d_r, d_c) :
                r_ = r+d_r_
                c_ = c+d_c_
                
                if not(0 <= r_ < len(board) and 0 <= c_ < len(board[0])) :
                    continue
                    
                if board[r_][c_] == 1 :
                    continue
                    
                bomb_board[r_][c_] -= 1
                    
    answer = 0
    for r in range(len(board)) :
        for c in range(len(board[0])) :
            if bomb_board[r][c] == 0 :
                answer += 1
    
    return answer