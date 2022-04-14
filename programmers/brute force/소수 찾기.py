# First Trial
# Test Passed

from itertools import permutations

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    dict = {}
    # if "2" in numbers:
    #     answer += 1
    # odds = [x for x in numbers if int(x) % 2 == 1]
    # print(odds)
    
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
        # for num in list(permutations(odds, i)):
            # print(''.join(num))
            temp = int(''.join(num))
            if isPrime(temp) and temp not in dict:
                dict[temp] = True
                answer += 1
    return answer



# ==================================================
# Other's Solution
# Test Passed

from itertools import permutations

def solution(numbers):
    primes = set()
    
    for i in range(len(numbers)):
        primes |= set(map(int, map("".join, permutations(numbers, i + 1))))
        primes -= set(range(0, 2))
    for i in range(2, int(max(primes) ** 0.5) + 1):
        primes -= set(range(i * 2, max(primes) + 1, i))
    return len(primes)