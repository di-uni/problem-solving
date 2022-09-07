# First Trial - recursive

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def solution(n):
    return fib(n)




# Second Trial

def solution(n):
    prev, cur = 0, 1
    
    for i in range(2, n + 1):
        next = (prev % 1234567 + cur % 1234567) % 1234567
        prev = cur
        cur = next
    return cur
