# First Trial

import sys, math

num = sys.stdin.readline().rstrip()

while num != "0":
    yn = 1
    for i in range(math.floor(len(num)/2)):
        if num[i] != num[-i-1]:
            yn = 0
            print("no")
            break
    if yn == 1:
        print("yes")
    num = sys.stdin.readline().rstrip()

exit(0)

# Second Trial referred from other's solution

import sys, math

num = sys.stdin.readline().rstrip()

while num != "0":
    if num == num[::-1]:
        print("yes")
    else:
        print("no")
    num = sys.stdin.readline().rstrip()
exit(0)


# Third Trial referred from other's solution

import sys, math

while True:
    num = sys.stdin.readline().rstrip()

    if num == "0":
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")