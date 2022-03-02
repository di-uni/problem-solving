# First Trial
# Solved (메모리 30860 KB, 시간 68 ms)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")