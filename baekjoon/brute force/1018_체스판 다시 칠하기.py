N, M = map(int, input().split())
board = []
cnt = N * M
Bstart = "B"

for i in range(N):
    line = input()
    board.append(line)

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        # print(i, j)
        Wstart_cnt = 0
        Bstart_cnt = 0
        for w in range(8):
            if w % 2 == 0:
                Bstart = "B"
            else:
                Bstart = "W"
            for h in range(8):
                # print(w, h)
                if board[i + w][j + h] == Bstart:
                    Wstart_cnt += 1
                else:
                    Bstart_cnt += 1
                if Bstart == "B":
                    Bstart = "W"
                else:
                    Bstart = "B"
                # print(board[i + w][j + h], Bstart, Wstart_cnt, Bstart_cnt)
        # print(Wstart_cnt, Bstart_cnt)
        cnt = min(cnt, Wstart_cnt, Bstart_cnt)


print(cnt)
