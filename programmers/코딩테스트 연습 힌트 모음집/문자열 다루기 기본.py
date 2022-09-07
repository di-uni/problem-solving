def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for elem in s:
        if elem.isalpha():
            return False
    return True


# 개선 
def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    if s.isdigit():
        return True
    return False