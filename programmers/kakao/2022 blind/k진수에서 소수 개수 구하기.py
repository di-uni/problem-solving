def decimalToK(n, k):
    result = ''

    while n > 0:
        n, mod = divmod(n, k)
        result = str(mod) + result

    return result

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    # k 진수로 바꾸기
    # 0을 기준으로 split
    nums = decimalToK(n, k).split("0")
    # print(nums)
    
    # 소수인지 아닌지 판별하기
    for num in nums:
        if num.isdigit() and isPrime(int(num)):
            answer += 1
            
    return answer



# ==========================================
# Other's Solution
# using string library

import string

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
    
    knum = convert(n, k)
    
    for num in knum.split("0"):
        if num and isPrime(int(num)):
            answer += 1
    
    return answer