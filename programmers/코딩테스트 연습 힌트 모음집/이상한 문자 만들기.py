def solution(s):
    answer = ''
    idx = 0
    for char in s:
        if char.isspace():
            answer += char
            idx = 0
            continue
        if idx % 2 == 0:
            answer += char.upper()
        else:
            answer += char.lower()
        idx += 1
            
    return answer


# ==========================================
# Other's Solution
# using split

def solution(s):
    answer = ''
    slist = s.split(" ")
    
    for word in slist:
        for i, w in enumerate(word):
            if i % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()
        answer += " "
    
    return answer[0:-1]