# 2022.10.09
# First Trial
# 50점 (시간 초과)

N = int(input())
M = int(input())
s = input()
P = "I"+"OI" * N
ans = 0

for i in range(M - len(P) + 1):
    if s[i:i+len(P)] == P:
        ans += 1
print(ans)


# =========================
# Other's solution
# Solved (메모리 32796 KB, 시간 284 ms)

N = int(input())
M = int(input())
s = input()
ans, i, cnt = 0, 0, 0

while i < M - 1:
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
        
print(ans)