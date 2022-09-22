import re

def solution(new_id):
    # 1, 2단계
    answer = re.sub("[^a-z0-9\.\-\_]", "", new_id.lower())
    
    # 3, 4단계
    answer = re.sub('\.+', '.', answer).strip(".")
    
    # 5단계
    if answer == "":
        answer = "a"
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")
    # 7단계
    elif len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer