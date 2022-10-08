# First Trial
# Solved (메모리 30864 KB, 시간 68 ms)

M = 1234567891
r = 31

L = int(input())
word = input()
ans = 0

for i, w in enumerate(word):
    ans += (ord(w) - 96) * (r ** i)

print(ans % M)

# ===================================
# Other's solution
# alphabet에 번호를 부여하는 방법이 달라서 가져옴
# Solved (메모리 30864 KB, 시간 72 ms)

apb = "abcdefghijklmnopqrstuvwxyz"
M = 1234567891
r = 31

L = int(input())
word = input()
ans = 0

for i, w in enumerate(word):
    ans += (apb.find(w) + 1) * (r ** i)

print(ans % M)