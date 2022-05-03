# First Trial
# Solved (메모리 35868 KB, 시간 1732 ms)

N, M = map(int, input().split())
board = []
max_val = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if i < N - 1 and j < M - 1:
            square = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            max_val = max(max_val, square)

            if i < N - 2:
                # print(board[i][j])
                LorPink = board[i][j] + board[i+1][j] + board[i+2][j] + max(board[i+2][j+1], board[i+1][j+1], board[i][j+1])
                flippedLorPink =  board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + max(board[i+2][j], board[i+1][j], board[i][j])
                green = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
                flippedGreen = board[i][j+1] + board[i+1][j+1] + board[i+1][j] + board[i+2][j]
                max_val = max(max_val, LorPink, flippedLorPink, green ,flippedGreen)

            if j < M - 2:
                LorPink = board[i][j] + board[i][j+1] + board[i][j+2] + max(board[i+1][j+2], board[i+1][j+1], board[i+1][j])
                flippedLorPink =  board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + max(board[i][j+2], board[i][j+1], board[i][j])
                green = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
                flippedGreen = board[i+1][j] + board[i+1][j+1] + board[i][j+1] + board[i][j+2]
                max_val = max(max_val, LorPink, flippedLorPink, green ,flippedGreen)

        if i < N - 3:
            # print(board[i][j])
            line = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            max_val = max(max_val, line)

        if j < M - 3:
            line = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            max_val = max(max_val, line)

print(max_val)