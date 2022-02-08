cro = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
cro3 = ["dz="]

word = input()
i = 0
cnt = 0

while i < len(word):
    isCro = 0
    if i < len(word) - 2:
        if word[i:i+3] == cro3[0]:
            cnt += 1
            i += 3
            continue
    if i < len(word) - 1:
        for c in cro:
            if c == word[i:i+2]:
                cnt += 1
                i += 2
                isCro = 1
                break
    if isCro == 0:
        cnt += 1
        i += 1
print(cnt)
    