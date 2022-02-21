N = int(input())
ans = 0

for i in range(N):
    val = i
    temp = i
    # print("i: " + str(i))
    while temp > 0:
        val += temp % 10
        temp //= 10
        # print(val)
    if val == N:
        ans = i
        break

print(ans)