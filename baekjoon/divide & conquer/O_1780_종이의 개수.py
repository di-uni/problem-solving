# First Trial
# Solved (메모리 68804 KB, 시간 6376 ms)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 3

def dc(x, y, n):
    firstElem = arr[x][y]
    # print(x,y,n)

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != firstElem:
                for x_k in range(3):
                    for y_k in range(3):
                        dc(x + x_k * (n // 3), y + y_k * (n // 3), n // 3)
                return
    
    cnt[firstElem + 1] += 1

dc(0, 0, N)

for c in cnt:
    print(c)