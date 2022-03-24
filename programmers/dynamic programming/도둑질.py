# First Trial
# 정확성 Test Passed / 효율성 Test Failed

def solution(money):
    n = len(money)
    contain_first = money[0:n-1]
    contain_last = money[1:n]
    memo_first = {}
    memo_last = {}
    
    def rob(i, money, memo):
        if i == 0:
            return money[0]
        elif i == 1:
            return max(money[0], money[1])
        if i not in memo:
            memo[i] = max(rob(i - 1, money, memo), rob(i - 2, money, memo) + money[i])
        return memo[i]
    
    return max(rob(n-2, contain_first, memo_first), rob(n-2, contain_last, memo_last))

# Second Trial
# Test Passed

def solution(money):
    n = len(money)
    
    pprev1 = prev1 = 0
    pprev2 = prev2 = 0
    
    for i in range(len(money)):
        if i != 0:
            cur = max(prev1, pprev1 + money[i])
            pprev1, prev1 = prev1, cur
        if i != n - 1:
            cur = max(prev2, pprev2 + money[i])
            pprev2, prev2 = prev2, cur
    
    return max(prev1, prev2)


# ==============================
# Other's Solution

def solution(money):
    if len(money) == 3:
        return max(money)
    else:

        with0 = [money[0], money[1], money[0] + money[2], max(money[0], money[1]) + money[3]]
        wout0 = [money[1], money[2], money[1] + money[3]]
        for m in money[4:]:
            with0.append(max(with0[-2], with0[-3]) + m)
            wout0.append(max(wout0[-2], wout0[-3]) + m)

    return max(with0[-3], with0[-2], wout0[-1])