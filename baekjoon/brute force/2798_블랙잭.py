N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for x in range(len(cards)):
    for y in range(x + 1, len(cards)):
        for z in range(y + 1, len(cards)):
            temp = cards[x] + cards[y] + cards[z]
            if temp <= M:
                ans = max(ans, temp)
print(ans)