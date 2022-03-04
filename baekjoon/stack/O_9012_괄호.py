# First Trial
# Solved (메모리 30864 KB, 시간 80 ms)

T = int(input())

for _ in range(T):
    stack = []
    ps = input()
    isVPS = True    # Valid Parenthesis String
    for p in ps:
        if p == "(":
            stack.append(")")
        elif p == ")":
            if len(stack) == 0:
                isVPS = False
                break
            stack.pop()
    if len(stack) != 0:
        isVPS = False
    if isVPS:
        print("YES")
    else:
        print("NO")

# =====================================
# Other's Solution
# Solved (메모리 30864 KB, 시간 76 ms)

T = int(input())

for _ in range(T):
    stack = []
    ps = input()    # Valid Parenthesis String
    for p in ps:
        if p == "(":
            stack.append(")")
        elif p == ")":
            if len(stack) == 0:
                print("NO")
                break
            stack.pop()
    else:   # break문으로 끊기지 않고 수행됐을 경우 수행한다.
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
