# First Trial
# Time Limit Exceeded

# n = input()
# temp = n
# count = 0

# while True:
#     if int(temp) < 10:
#         temp = "0" + temp
#     new_temp = str(int(temp[0]) + int(temp[1]))
#     temp = temp[-1] + new_temp[-1]
#     count += 1
#     if n == temp:
#         break
        
# print(count)


# ==================================================================
# Second Trial

N = int(input())
temp = (N % 10) * 10 + (N % 10 + N // 10) % 10
cnt = 1
# print(temp)

while temp != N:
    temp = (temp % 10) * 10 + (temp % 10 + temp // 10) % 10
    cnt += 1
    # print(temp, cnt)

print(cnt)