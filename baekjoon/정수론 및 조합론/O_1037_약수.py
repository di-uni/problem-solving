# First Trial
# Solved (메모리 30864 KB, 시간 72 ms)

ali = int(input())
if ali == 1:
    print(int(input()) ** 2)
else:
    alis = list(map(int, input().split()))
    alis.sort()
    print(alis[0] * alis[ali - 1])

# ===================================
# Other's solution
# sort 대신 max, min 값을 구하면 더 간단하다!
# Solved (메모리 30864 KB, 시간 84 ms)

n = int(input())
alis = list(map(int, input().split()))
print(min(alis) * max(alis))