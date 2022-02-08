n = int(input())
cnt = 0

for num in range(1, n + 1):
    if num < 10:
        cnt += 1
        continue
    num = str(num)
    d = int(num[0]) - int(num[1])
    isEqualDiff = 1
    
    for i in range(1, len(num) - 1):
        if d != int(num[i]) - int(num[1 + 1]):
            isEqualDiff = 0
    if isEqualDiff == 1:
        cnt += 1

print(cnt)