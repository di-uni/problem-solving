# First Trial
# Test Passed

def solution(phone_book):
    answer = True
    dic = {}

    for num in phone_book:
        dic[hash(num)] = num

    for num in phone_book:
        temp = ''
        for i in num:
            temp += i
            if temp == num:
                continue
            if hash(temp) in dic:
                return False

    return answer

# Second Trial - Refine
# Test Passed

def solution(phone_book):
    answer = True
    dic = {}

    for num in phone_book:
        dic[hash(num)] = num

    for num in phone_book:
        temp = ''
        for i in num:
            temp += i
            if hash(temp) in dic and temp != num:
                answer = False

    return answer


# ==============================
# Other's Solution 
# use zip

def solution(phone_book):
    phone_book = sorted(phone_book)

    # sort 하면 접두어가 무조건 직전에 위치
    for p1, p2 in zip(phone_book, phone_book[1:]):
        # 1st round: p1 = phone_book[0], p1 = phone_book[0]
        # 2nd round: p1 = phone_book[1], p1 = phone_book[2]
        if p2.startswith(p1):
            return False

    return True