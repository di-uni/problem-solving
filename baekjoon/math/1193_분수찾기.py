n = int(input())
i = 1
first, second = 1, 1

# 1/1 
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1

while n > 0:
    n -= i
    # print(i, n+i)
    if n <= 0:
        if i % 2 == 0:
            # print("here")
            first, second = 1, i
            for k in range(n + i - 1):
                first += 1
                second -= 1
        else:
            first, second = i, 1
            for k in range(n + i - 1):
                first -= 1
                second += 1
    i += 1

print(str(first) + "/" + str(second))