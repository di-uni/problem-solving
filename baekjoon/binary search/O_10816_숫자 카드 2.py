# First Trial
# 시간 초과

N = int(input())
cards = sorted(list(map(int, input().split())))
check_card = set(cards)
M = int(input())
mine = list(map(int, input().split()))
ans = []

for m in mine:
    if m not in check_card:
        ans.append(str(0))
        continue
    print(ans)
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == m:
            cnt = 1
            i = 1
            j = -1
            for i in range(1, N - mid):
                print(mid, i)
                if cards[mid + i] == m:
                    cnt += 1
                else:
                    break
            for i in range(-1, -mid-1, -1):
                print(mid, i)
                if cards[mid + i] == m:
                    cnt += 1
                else:
                    break
            ans.append(str(cnt))
            break
        elif cards[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

print(" ".join(ans))


# Second Trial with hint (using dictionary, bisect, or 20000001 array)
# Using dictionary
# 시간 초과

import sys

N = int(sys.stdin.readline().rstrip())
cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

check_card = set(cards)
ans = []
card_dict = {}

for m in mine:
    if m in card_dict:
        ans.append(card_dict[m])
        continue
    if m not in check_card:
        ans.append(str(0))
        card_dict[m] = str(0)
        continue
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == m:
            cnt = cards.count(m)
            ans.append(str(cnt))
            card_dict[m] = str(cnt)
            break
        elif cards[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

print(" ".join(ans))


# Third Trial with hint (using dictionary, bisect, or 20000001 array)
# Using dictionary
# Solved (메모리 115408 KB, 시간 1024 ms)

import sys

N = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

card_dict = {}

for card in cards:
    if card not in card_dict:
        card_dict[card] = 0
    card_dict[card] += 1

for m in mine:
    if m not in card_dict:
        print(0, end=" ")
    else:
        print(card_dict[m], end=" ")



# Forth Trial with hint
# Using bisect
# Solved (메모리 114704 KB, 시간 1860 ms)

import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline().rstrip())
cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

card_dict = {}

for m in mine:
    if m not in card_dict:
        cnt = bisect_right(cards, m) - bisect_left(cards, m)
        # print(m, bisect_right(cards, m), bisect_left(cards, m))
        print(cnt, end=" ")
        card_dict[m] = cnt
    else:
        print(card_dict[m], end=" ")


# ======================================
# Other's Solution
# Using Counter 
# (input의 원소-key-들이 input에서 몇 번 등장했는지-value-를 딕셔너리 형태로 반환)
# Solved (메모리 111676 KB, 시간 1112 ms)

import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = Counter(cards)

for m in mine:
    if m in cnt:
        print(cnt[m], end=' ')
    else:
        print(0, end=' ')
        