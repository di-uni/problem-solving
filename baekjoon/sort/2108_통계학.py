import sys

N = int(sys.stdin.readline().rstrip())
num = []
numdict = {}
modelist = []

for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))
    if num[i] not in numdict:
        numdict[num[i]] = 0
    numdict[num[i]] += 1
num.sort()
mode_value = max(numdict.values())
for key, value in numdict.items():
    if value == mode_value:
        modelist.append(key)
# print(numdict, mode_value, modelist)
modelist.sort()
mode = modelist[0]
if len(modelist) > 1:
    mode = modelist[1]

print(round(sum(num) / N))
print(num[int(N/2)])
print(mode)
print(num[N-1] - num[0])