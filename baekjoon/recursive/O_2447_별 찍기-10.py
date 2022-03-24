# First Trial
# Solved (메모리 67588 KB, 시간 3876 ms)

N = int(input())
ans = [[True]*N for _ in range(N)]

def make_pattern(n, r, ans):
    m = n // 3
    for x in range(r):
        for y in range(r):
            for i in range(m, 2 * m):
                for j in range(m, 2 * m):
                    ans[n * x + i][n * y + j] = False
    if n != 1: make_pattern(n // 3, r * 3, ans)

make_pattern(N, 1, ans)

for line in ans:
    for l in line:
        if l: print("*", end="")
        else: print(" ", end="")
    print()


# =========================
# Other's solution
# Solved (메모리 40208 KB, 시간 76 ms)

import sys
sys.setrecursionlimit(10**6)
# 만약 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다. 
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 
# 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 
# 코딩테스트 환경에서는 에러 메시지를 볼 수 없다.

def append_star(n):
    if n == 1:
        return ['*']

    stars = append_star(n // 3)
    ans = []

    for s in stars:
        ans.append(s*3)
    for s in stars:
        ans.append(s + ' '*(n // 3) + s)
    for s in stars:
        ans.append(s*3)
    return ans

N = int(sys.stdin.readline().rstrip())
print('\n'.join(append_star(N)))