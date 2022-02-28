max_num = 123456 * 2 + 1
prime = [True] * max_num
n = int(input())
largest = 2
prime[1] = False

while n != 0:
    temp = int((2 * n) ** 0.5)
    if largest < temp:
        for i in range(largest, temp + 1):
            if prime[i]:
                for j in range(i * 2, max_num, i):
                    prime[j] = False
        largest = temp

    # mapreduce 사용
    # print(prime[n+1:2*n], temp)
    ans = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            ans += 1
    print(ans)
    n = int(input())
    


