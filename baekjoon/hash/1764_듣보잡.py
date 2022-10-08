# First Trial
# Solved (메모리 37756 KB, 시간 112 ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
heardSeen = []

for _ in range(N):
    dict[input().rstrip()] = True

for _ in range(M):
    seen = input().rstrip()
    if seen in dict:
        heardSeen.append(seen)

print(len(heardSeen))
for name in sorted(heardSeen):
    print(name)


# ===================================
# Other's solution
# use set
# Solved (메모리 42108 KB, 시간 120 ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = set([input().rstrip() for _ in range(N)])
b = set([input().rstrip() for _ in range(M)])

result = sorted(list(a & b))

print(len(result))
for i in result:
    print(i)