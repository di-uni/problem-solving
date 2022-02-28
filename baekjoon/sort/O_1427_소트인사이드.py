# First Trial
# Solved

N = input()
list_n = [int(n) for n in N]
list_n.sort(reverse=True)
ans = ""

for n in list_n:
    ans += str(n)

print(ans)

# =========================
# Other's solution

N = input()
list_n = [int(n) for n in N]
list_n.sort(reverse=True)

# ans 변수 대신 한 번에 프린트 하기
for n in list_n:
    print(n, end='')
