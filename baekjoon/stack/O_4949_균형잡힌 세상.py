# First Trial
# Solved (메모리 30860 KB, 시간 364 ms)

while True:
    sentence = input()
    if sentence == ".":
        break

    stack = []
    isVPS = True
    for s in sentence:
        if s == "(":
            stack.append(")")
        elif s == ")":
            if len(stack) > 0 and stack[-1] == s:
                stack.pop()
            else:
                isVPS = False
                break
        elif s == "[":
            stack.append("]")
        elif s == "]":
            if len(stack) > 0 and stack[-1] == s:
                stack.pop()
            else:
                isVPS = False
                break
    if len(stack) != 0:
        isVPS = False
    if isVPS:
        print("yes")
    else:
        print("no")


# =====================================
# Other's Solution
# Solved (메모리 30860 KB, 시간 360 ms)

while True:
    sentence = input()
    if sentence == ".":
        break

    stack = []
    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif s == "[":
            stack.append("]")
        elif s == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")