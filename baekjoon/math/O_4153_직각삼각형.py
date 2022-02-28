# First Trial
# Solved

side = list(map(int, input().split()))

while side[0] != 0 or side[1] != 0 or side[2] != 0:
    side.sort()
    if side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
        print("right")
    else:
        print("wrong")
    side = list(map(int, input().split()))


# =========================
# Other's solution
# sort는 시간복잡도가 크므로 max와 remove 사용하기

side = list(map(int, input().split()))

while side[0] != 0 or side[1] != 0 or side[2] != 0:
    max_side = max(side)
    side.remove(max_side)
    if side[0] ** 2 + side[1] ** 2 == max_side ** 2:
        print("right")
    else:
        print("wrong")
    side = list(map(int, input().split()))