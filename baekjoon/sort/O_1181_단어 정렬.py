# First Trial
# Done but complicate

import sys

N = int(sys.stdin.readline().rstrip())
word = {}

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    if len(temp) not in word:
        word[len(temp)] = []
    if temp not in word[len(temp)]:
        word[len(temp)].append(temp)

word_len = sorted(word.keys())

for l in word_len:
    if len(word[l]) == 1:
        print(word[l][0])
    elif len(word[l]) > 1:
        word[l].sort()
        for w in word[l]:
            print(w)

# Second Trial referred from other's solution

import sys

N = int(sys.stdin.readline().rstrip())
word = []

for i in range(N):
    word.append(sys.stdin.readline().rstrip())

word = list(set(word))    # 중복 문자 제거
word.sort()
word.sort(key = len)  # 문자열 길이 순으로 정렬

for w in word:
    print(w)

