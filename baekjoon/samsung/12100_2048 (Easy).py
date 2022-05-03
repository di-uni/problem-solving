from collections import deque

N = int(input())
board = []
queue = deque([])

for _ in range(N):
    board.append(list(map(int, input().split())))

print(board)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


cur_board = queue.popleft()
for k in range(4):
    new_board = []
    for i in range(N):
        temp_line = []
        for j in range(N):
            if cur_board[i][j] == cur_board[i + dx[k]][j + dx[k]]:
                temp_line.append(cur_board[i][j] * 2)
            elif cur_board[i + dx[k]][j + dx[k]] != 0:
                temp_line.append(cur_board[i + dx[k]][j + dx[k]])

                
