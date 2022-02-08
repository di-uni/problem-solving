word = input().upper()
alpha = [0] * 26

for w in word:
    alpha[ord(w) - 65] += 1

maxVal = max(alpha)
maxIdx = [i for i, val in enumerate(alpha) if val == maxVal]
if len(maxIdx) > 1:
    print("?")
else:
    print(chr(maxIdx[0] + 65))
