n = int(input())

for i in range(n):
    time, word = input().split()
    time = int(time)
    ans = ""
    for w in word:
        ans += w * time
    print(ans)