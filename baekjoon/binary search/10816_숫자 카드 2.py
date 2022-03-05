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

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
mine = list(map(int, input().split()))

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