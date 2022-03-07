# First Trial
# Using Binary Search
# 시간 초과

N = int(input())
cards = sorted(set(list(map(int, input().split()))))
M = int(input())
mine = list(map(int, input().split()))

ans = []
card_dict = {}

for m in mine:
    print(m)
    if m in card_dict:
        ans.append(card_dict[m])
        continue
    if m not in cards:
        ans.append(str(0))
        card_dict[m] = str(0)
        continue
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if cards[mid] == m:
            ans.append(str(1))
            card_dict[m] = str(1)
            break
        elif cards[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

print(" ".join(ans))

# Second Trial
# Solved (메모리 112452 KB, 시간 4132 ms)

import sys

N = int(sys.stdin.readline().rstrip())
cards = sorted(set(list(map(int, sys.stdin.readline().rstrip().split()))))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

card_dict = {}

for m in mine:
    if m in card_dict:
        print(card_dict[m], end=' ')
        continue
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == m:
            print(1, end=' ')
            card_dict[m] = 1
            break
        elif cards[mid] < m:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(0, end=' ')


# Third Trial
# Using Dictionary
# Solved (메모리 123668 KB, 시간 684 ms)

import sys

N = int(sys.stdin.readline().rstrip())
cards = set(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
mine = list(map(int, sys.stdin.readline().rstrip().split()))

card_dict = {}

for m in mine:
    if m in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')