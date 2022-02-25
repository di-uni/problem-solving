# First Trial

import math

N = int(input())
ans = []

three = N / 3
if N % 3 == 0:
    ans.append(int(three))

five = N / 5
if N % 5 == 0:
    ans.append(int(five))

for i in range(math.floor(five), math.ceil(three)):
    for j in range(i):
        if 5 * j + 3 * (i - j) == N:
            ans.append(i)
            break

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))


# Second Trial referred to other's solution
# Greedy 

# ver.1
N = int(input())
cnt = 0

if N % 5 == 0:
    print(int(N / 5))
else:
    cnt = 0
    while N % 5 != 0:
        if N < 3:
            print(-1)
            exit(0)
        N -= 3
        cnt += 1
    print(int(N / 5) + cnt)

# ver.2
N = int(input())
cnt = 0

while N % 5 != 0:
    if N < 3:
        print(-1)
        exit(0)
    N -= 3
    cnt += 1
print(int(N / 5) + cnt)

# ver.3 (other's solution)
N = int(input())
ans = 0

while N >= 0:
    if N % 5 == 0:
        ans += N // 5
        print(ans)
        break
    N -= 3
    ans += 1
else:
    print(-1)



    