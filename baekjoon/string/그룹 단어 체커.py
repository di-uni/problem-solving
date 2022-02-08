n = int(input())
cnt = 0

for i in range(n):
    cnt += 1
    word = input()
    alpha = [0] * 26
    prev = word[0]
    alpha[ord(prev) - 97] = 1

    for i in range(1, len(word)):
        if prev != word[i]: 
            if alpha[ord(word[i]) - 97] == 0:
                alpha[ord(word[i]) - 97] = 1
            else:
                # print(i, word, word[i])
                cnt -= 1
                break
        prev = word[i]
print(cnt)
