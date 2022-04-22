# First Trial
# Solved (메모리 30840 KB, 시간 76 ms)

N = int(input())
cnt = 0

for i in range(1, N + 1):
    temp = i
    while True:
        if temp % 5 == 0:
            temp //= 5
            cnt += 1
        else: 
            break
print(cnt)


# ===================================
# Other's solution (1)
# 5로 나눠지는 몫을 더해주는 방법 (5!: 1개,  10!: 2개, 25!: 5+1개)
# Solved (메모리 30840 KB, 시간 68 ms)

N = int(input())
cnt = 0

while N >= 5:
    cnt += N // 5
    N //= 5

print(cnt)