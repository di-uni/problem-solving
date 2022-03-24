# First Trial
# Solved (메모리 32972 KB, 시간 68 ms)

import sys, math

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, N):
    if nums[0] % nums[i] == 0:
        print(f'{nums[0] // nums[i]}/1')
    else:
        gcd = math.gcd(nums[0], nums[i])
        print(f'{nums[0]//gcd}/{nums[i]//gcd}')



# ===========================================
# Other's Solution
# 유클리드 호제법 이용
# Solved (메모리 30860 KB, 시간 72 ms)

import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

def GCD(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

for i in range(1, N):
    gcd = GCD(nums[0], nums[i])
    print(f'{nums[0]//gcd}/{nums[i]//gcd}')
