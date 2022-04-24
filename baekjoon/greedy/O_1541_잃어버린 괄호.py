#  First Trial
# Solved (메모리 30840 KB, 시간 72 ms)

formula = input()
temp = ""
nums = []
plusMinus = []

for c in formula:
    if c == "+" or c == "-":
        nums.append(int(temp))
        temp = ""
        plusMinus.append(c)
    else:
        temp += c
nums.append(int(temp))

isMinus = False
for i, s in enumerate(plusMinus):
    if s == "-":
        isMinus = True
    else:
        if isMinus:
            plusMinus[i] = "-"

total = nums[0]

for i in range(1, len(nums)):
    if plusMinus[i - 1] == "+":
        total += nums[i]
    else:
        total -= nums[i]

print(total)



# ===================================
# Other's solution 
# split 사용
# Solved (메모리 30840 KB, 시간 68 ms)

formula = input().split("-")
ans = 0

for i in formula[0].split("+"):
    ans += int(i)

for i in formula[1:]:
    for j in i.split("+"):
        ans -= int(j)

print(ans)
    