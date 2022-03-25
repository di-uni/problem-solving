# First Trial
# Solved (메모리 30864 KB, 시간 72 ms)

import sys

N = int(sys.stdin.readline().rstrip())
arr = [[] for i in range(N)]
ans = ""

for i in range(N):
    for s in sys.stdin.readline().rstrip():
        arr[i].append(s)

def dc(x, y, n):
    global ans
    firstElem = arr[x][y]
    if n == 1:
        if firstElem == '1':
            ans += '1'
        else:
            ans += '0'
        return
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if firstElem != arr[i][j]:
                ans += '('
                dc(x, y, n // 2)
                dc(x, y + n // 2, n // 2)   # i가 y축, j가 x축
                dc(x + n // 2, y, n // 2)
                dc(x + n // 2, y + n // 2, n // 2)
                ans += ')'
                return
    if firstElem == '1':
        ans += '1'
    else:
        ans += '0'

dc(0, 0, N)
print(ans)


# =======================================================
# Other's solution
# firstElem 체크 경우의 수 단순화, print end 이용
# Solved (메모리 30864 KB, 시간 76 ms)

import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, input())) for _ in range(N)]

def dc(x, y, n):
    firstElem = arr[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if firstElem != arr[i][j]:
                print('(', end='')
                dc(x, y, n // 2)
                dc(x, y + n // 2, n // 2)   # i가 y축, j가 x축
                dc(x + n // 2, y, n // 2)
                dc(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return

    if firstElem == 1:
        print(1, end='')
    else:
        print(0, end='')

dc(0, 0, N)
