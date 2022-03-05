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