# First Trial
# Solved (메모리 49708 KB, 시간 200 ms)

N = int(input())
A = set(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

for x in X:
    if x in A:
        print(1)
    else:
        print(0)


# ===================================
# Second Trial
# Binary Search 사용
# Solved (메모리 47212 KB, 시간 784 ms)

N = int(input())
A = sorted(list(set(map(int, input().split()))))
M = int(input())
X = list(map(int, input().split()))

def bin(left, right, target):
    # print(left, right, target)
    if left > right:
        print(0)
        return
    mid = (left + right) // 2
    if A[mid] == target:
        print(1)
    elif A[mid] > target:
        bin(left, mid - 1, target)
    else:
        bin(mid + 1, right, target)

for x in X:
    bin(0, len(A) - 1, x)


# ===================================
# Other's Solution
# Binary Search 사용: while문을 이용해 간단히, recursive 없이 풀이
# Solved (메모리 47216 KB, 시간 628 ms)

N = int(input())
A = sorted(list(set(map(int, input().split()))))
N = len(A)
M = int(input())
X = list(map(int, input().split()))

def bin(target):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return True
        elif target < A[mid]:
            right = mid - 1
        else: 
            left = mid + 1

for x in X:
    if bin(x):
        print(1)
    else:
        print(0)