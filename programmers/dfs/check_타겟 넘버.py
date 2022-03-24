# First Trial
# Test Passed

def solution(numbers, target):
    dp = {}

    def cal(_numbers, _target):
        n = len(_numbers)
        if (n, _target) in dp:
            return dp[(n, _target)]
        if n == 1:
            if abs(_target) == abs(_numbers[0]):
                return 1
            return 0
        else:
            dp[(n, _target)] = cal(_numbers[1:n + 1], _target - _numbers[0]) + cal(_numbers[1:n + 1], _target + _numbers[0])
            return dp[(n, _target)]


    return cal(numbers, target)



# ==============================
# Other's Solution (1)

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# Other's Solution (2)

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)