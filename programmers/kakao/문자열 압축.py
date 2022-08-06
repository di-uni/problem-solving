# First Trial
# Test Passed

def solution(s):
    min_len = float("inf")
    
    if len(s) == 1:
        return 1
    
    for d in range(1, len(s)//2 + 1):
        i = 0
        prev = ""
        txt = ""
        cnt = 0
        while i < len(s):
            if prev != "":
                if prev == s[i:i+d]:
                    cnt += 1
                elif cnt > 0:
                    txt += str(cnt + 1) + prev
                    cnt = 0
                else:
                    txt += prev
            prev = s[i:i+d]
            i += d
        if cnt > 0: txt += str(cnt + 1)
        txt += prev
        # print(txt)
        min_len = min(min_len, len(txt))
    return min_len



# ==========================================
# Other's Solution

def solution(s):
    min_len = float("inf")

    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        txt = ''
        cnt = 1
        prev = s[:i]

        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    txt += str(cnt) + prev
                else:
                    txt += prev
                prev = s[j:j+i]
                cnt = 1
        if cnt != 1:
            txt += str(cnt) + prev
        else:
            txt += prev
        min_len = min(min_len, len(txt))

    return min_len