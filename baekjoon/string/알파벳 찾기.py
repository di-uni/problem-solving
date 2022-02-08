word = input()
alpha = [-1] * 26
ans = ""

for i, w in enumerate(word):
    idx = int(ord(w)) - 97
    if alpha[idx] == -1:
        alpha[idx] = i
for a in alpha:
    ans += str(a)
    ans += " "
print(ans.rstrip())