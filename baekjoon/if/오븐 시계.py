h, m = map(int, input().split())
add = int(input())

time = h * 60 + m + add
if time >= 24 * 60:
    time -= 24 * 60
print(time // 60, time % 60)