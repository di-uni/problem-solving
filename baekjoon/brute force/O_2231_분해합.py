# First Trial
# Solved

N = int(input())
ans = 0

for i in range(N):
    val = i
    temp = i
    while temp > 0:
        val += temp % 10
        temp //= 10
    if val == N:
        ans = i
        break

print(ans)


# =========================
# Other's solution

N = int(input())

for i in range(1, N + 1):
    val = sum(map(int, str(i))) # map을 이용하여 간편하게 계산!
    val += i
    if val == N:
        print(i)
        break
    if i == N:  # 생성자와 i가 같다는 것은 생성자가 없다는 뜻
        print(0)