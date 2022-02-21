num = list(map(int, input().split()))
cal = 0

for n in num:
    cal += n * n

print(cal % 10)