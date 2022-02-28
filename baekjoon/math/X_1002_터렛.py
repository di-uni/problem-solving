# First Trial
# Failed

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

# Second Trial referred to other's solution

# 두 개의 원의 교점의 개수 구하기