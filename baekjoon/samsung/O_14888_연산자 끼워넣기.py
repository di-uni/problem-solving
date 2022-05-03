# First Trial
# Solved (메모리 525880 KB, 시간 1372 ms)

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
num_first = nums.pop(0)

op = ["+", "-", "x", "%"]
op_nums = list(map(int, input().split()))

operators = []
min_val = float("inf")
max_val = float("-inf")

for i in range(len(op_nums)):
    for _ in range(op_nums[i]):
        operators.append(op[i])

# print(operators)

for k in set(list(permutations(operators, len(operators)))):
    # print(k)
    val = num_first
    for op, num in zip(k, nums):
        if op == "+":
            val += num
        elif op == "-":
            val -= num
        elif op == "x":
            val *= num
        elif op == "%":
            if val < 0:
                val = -(-val // num)
            else:
                val //= num
            
    # print(val)
    min_val = min(min_val, val)
    max_val = max(max_val, val)

if min_val == float("inf"):
    min_val = max_val
if max_val == float("-inf"):
    max_val = min_val

print(max_val)
print(min_val)


# ===================================
# Other's solution 
# dfs 사용
# Solved (메모리 30840 KB, 시간 136 ms)

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = float("inf")
max_val = float("-inf")

def dfs(i, arr):
    global add, sub, mul, div, min_val, max_val
    if i == N:
        min_val = min(min_val, arr)
        max_val = max(max_val, arr)
    else: 
        if add > 0:
            add -= 1
            dfs(i + 1, arr + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(arr / nums[i]))
            div += 1

dfs(1, nums[0])

print(max_val)
print(min_val)