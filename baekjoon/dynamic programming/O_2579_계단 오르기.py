# First Solution
# Bottom-up
# Solved (메모리 30840 KB, 시간 72 ms)

def getMaxScores(n, stairs):
    dp = [0] * n

    if n == 1:
        print(stairs[0])
        return
    if n == 2:
        print(stairs[0]+stairs[1])
        return 

    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]
    for i in range(n-3):
        dp[i+3] = max(dp[i]+stairs[i+2], dp[i+1])+stairs[i+3]
    # print(dp)
    print(dp[-1]) 

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

getMaxScores(n, stairs)