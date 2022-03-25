# First Trial
# Solved (메모리 30864 KB, 시간 88 ms)

import sys

N = int(sys.stdin.readline().rstrip())
arr = []
w_cnt = 0
b_cnt = 0

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))


def dq(i_start, i_end, j_start, j_end):
    firstElem = arr[i_start][j_start]
    global w_cnt, b_cnt

    if i_start == i_end and j_start == j_end:
        if firstElem:   b_cnt += 1
        else: w_cnt += 1
        return

    for i in range(i_start, i_end):
        for j in range(j_start, j_end):
            if arr[i][j] != firstElem:
                half = (i_end - i_start) // 2
                dq(i_start, i_start + half, j_start, j_start + half)
                dq(i_start, i_start + half, j_start + half, j_end)
                dq(i_start + half, i_end,  j_start, j_start + half)
                dq(i_start + half, i_end, j_start + half, j_end)
                return
    if firstElem:   b_cnt += 1
    else: w_cnt += 1

dq(0, N, 0, N)
print(w_cnt)
print(b_cnt)


# =======================================================
# Other's solution
# size n을 파라미터로
# Solved (메모리 30864 KB, 시간 100 ms)

import sys
input = sys.stdin.readline

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
w_cnt = b_cnt = 0

def div_conq(x, y, n):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if B[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == n ** 2:
        b_cnt += 1
    else:
        div_conq(x, y, n // 2)
        div_conq(x + n // 2, y, n // 2)
        div_conq(x, y + n // 2, n // 2)
        div_conq(x + n // 2, y + n // 2, n // 2)
    return

div_conq(0, 0, N)
print(w_cnt)
print(b_cnt)