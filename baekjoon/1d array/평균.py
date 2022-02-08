n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
mean = 0

for s in scores:
    mean += s/m * 100
print(mean/n)