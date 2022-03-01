# First Trial
# Wrong Answer

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print('here?')
            print(-1)   # 있을 수 있는 위치의 개수가 무한대
        else:
            print('here?')
            print(0)    # 있을 수 있는 위치의 경우의 수 없음
        continue
    elif x1 == x2:
        y = (r1 ** 2 - r2 ** 2 - y1 ** 2 + y2 ** 2) / (2 * (y2 -y1))
        if x1 ** 2 + (y - y1) ** 2 == r1 ** 2:
            print(1)    # 가능한 x값이 0인 경우
        else:
            print(2)    # 0이 아닌 경우 +, - 값 두 가지 존재
        continue
    elif y1 == y2:
        x = (r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2) / (2 * (x2 -x1))
        if y1 ** 2 + (x - x1) ** 2 == r1 ** 2:
            print(1)    # 가능한 y값이 0인 경우
        else:
            print(2)    # 0이 아닌 경우 +, - 값 두 가지 존재
        continue
    print(-1)


# ==========================================
# Second Trial (with hint)
# hint: 두 개의 원의 교점의 개수 구하기
# Solved (메모리 30860 KB, 시간 84 ms)

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d == 0:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    if d > r1 + r2 or d < abs(r1 - r2):
        print(0)
        continue
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
        continue
    else:
        print(2)

# ==========================================
# Other's solution
# 묶을 수 있는 건 최대한 묶기 (print(0)을 마지막 else로 한 번에 처리)
# Solved (메모리 30860 KB, 시간 88 ms)

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d == 0 and r1 == r2:
        print(-1)
        continue
    if d < r1 + r2 and d > abs(r1 - r2):
        print(2)
        continue
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
        continue
    else:
        print(0)
