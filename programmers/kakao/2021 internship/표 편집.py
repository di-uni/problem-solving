# First Trial
# 정확성 Test Passed, 효율성 Test Failed (50%)

def solution(n, k, cmd):
    nums = [True] * n
    z = []
    cur = k
    last = n - 1
    answer = ''
    
    for c in cmd:
        if c == "C":
            z.append(cur)
            nums[cur] = False
            if last == cur:
                while not nums[cur]:
                    cur -= 1
                last = cur
            else:
                while not nums[cur]:
                    cur += 1
            # print(cur)
        elif c == "Z":
            z_val = z.pop()
            nums[z_val] = True
            if z_val > last:
                last = z_val
        else:
            upDown, amount = c.split()
            amount = int(amount)
            if upDown == "U":
                for i in range(amount):
                    cur -= 1
                    while not nums[cur]:
                        # print(nums[cur], cur)
                        cur -= 1
                    # print(nums[cur], cur)
                
            elif upDown == "D":
                for i in range(amount):
                    cur += 1
                    while not nums[cur]:
                        # print(nums[cur], cur)
                        cur += 1
                    # print(nums[cur], cur)
                    
    for i in nums:
        if i:
            answer += "O"
        else:
            answer += "X"
            
    return answer


# ==========================================
# Other's Solution
# Save up, down info in dict

def solution(n, k, cmd):
    cur = k
    table = { i: [i-1, i+1] for i in range(n) }     # up, down 정보 함께 저장 
    answer = ['O'] * n

    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]

    stack = []

    for c in cmd:
        if c == "C":
            answer[cur] = 'X'
            prev, next = table[cur]
            # prev, next = table.pop(cur, None)
            stack.append([prev, cur, next])

            if next == None:
                cur = prev
                table[cur][1] = None
            else:
                cur = next
                if prev == None:
                    table[next][0] = None
                elif next == None:
                    table[prev][1] = None
                else:
                    table[prev][1] = next
                    table[next][0] = prev

        elif c == "Z":
            prev, z_val, next = stack.pop()
            answer[z_val] = 'O'
            
            if prev != None:
                table[prev][1] = z_val 
            if next != None:
                table[next][0] = z_val 

        else:
            upDown, amount = c.split()
            amount = int(amount)
            if upDown == "U":
                for _ in range(amount):
                    cur = table[cur][0]
            elif upDown == "D":
                for _ in range(amount):
                    cur = table[cur][1]

    return "".join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))