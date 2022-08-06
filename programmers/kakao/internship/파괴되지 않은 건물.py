# First Trial
# 정확성 테스트 Passed, 효율성 테스트 Failed

def solution(board, skill):
    answer = 0
    destroy = []
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree = -degree
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += degree
                if board[i][j] <= 0:
                    if [i, j] not in destroy:
                        destroy.append([i, j])
                else:
                    if [i, j] in destroy:
                        destroy.remove([i, j])
    
    # for line in board:
    #     for b in line:
    #         if b > 0:
    #             answer += 1
    
    # print(destroy)
    answer = len(board) * len(board[0]) - len(destroy)
    
    return answer


# ==========================================
# Second Trial referred to Other's Solution
# using prefix sum

def solution(board, skill):
    answer = 0
    prefix_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree = -degree
        prefix_board[r1][c1] += degree
        prefix_board[r2+1][c1] -= degree
        prefix_board[r1][c2+1] -= degree
        prefix_board[r2+1][c2+1] += degree
    
    # print(prefix_board)
    
    for i in range(len(prefix_board)):
        prefix_sum = 0
        for j in range(len(prefix_board[0])):
            prefix_sum += prefix_board[i][j]
            prefix_board[i][j] = prefix_sum
    
    for j in range(len(prefix_board[0])):
        prefix_sum = 0
        for i in range(len(prefix_board)):
            prefix_sum += prefix_board[i][j]
            prefix_board[i][j] = prefix_sum
    # print(prefix_board)
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_board[i][j]
            if board[i][j] > 0:
                answer += 1
        
    
    return answer


# Other's Solution
# using prefix sum

def solution(board, skill):
    answer = 0
    prefix_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree = -degree
        prefix_board[r1][c1] += degree
        prefix_board[r2+1][c1] -= degree
        prefix_board[r1][c2+1] -= degree
        prefix_board[r2+1][c2+1] += degree
    
    # Second Trial과 다른점 !! 
    for i in range(len(prefix_board) - 1):
        for j in range(len(prefix_board[0]) - 1):
            prefix_board[i][j + 1] += prefix_board[i][j]
    
    for j in range(len(prefix_board[0]) - 1):
        for i in range(len(prefix_board) - 1):
            prefix_board[i + 1][j] += prefix_board[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_board[i][j]
            if board[i][j] > 0:
                answer += 1
        
    
    return answer