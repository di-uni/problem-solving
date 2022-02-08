word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
ans = 0

for w in word:
    for i, d in enumerate(dial):
        if w in d:
            ans += i + 3
            break

print(ans)