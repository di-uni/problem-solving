def solution(survey, choices):
    types = ['RT', 'CF', 'JM', 'AN']
    result = {}
    answer = ''
    
    for choice, score in zip(survey, choices):
        score -= 4
        if score < 0:
            if choice[0] not in result:
                result[choice[0]] = 0
            result[choice[0]] -= score
        if score > 0:
            if choice[1] not in result:
                result[choice[1]] = 0
            result[choice[1]] += score
    
    # print(result)
    
    for ty in types:
        res_ty = [0, 0]
        if ty[0] in result:
            res_ty[0] = result[ty[0]]
        if ty[1] in result:
            res_ty[1] = result[ty[1]]
        if res_ty[0] < res_ty[1]:
            answer += ty[1]
        else: 
            answer += ty[0]
    return answer



# 개선
from collections import defaultdict

def solution(survey, choices):
    types = ['RT', 'CF', 'JM', 'AN']
    result = defaultdict(int)
    answer = ''
    
    for choice, score in zip(survey, choices):
        if score < 4:
            result[choice[0]] += 4 - score
        if score > 4:
            result[choice[1]] += score - 4
    
    for ty in types:
        res_ty = [0, 0]
        if ty[0] in result:
            res_ty[0] = result[ty[0]]
        if ty[1] in result:
            res_ty[1] = result[ty[1]]
        if res_ty[0] < res_ty[1]:
            answer += ty[1]
        else: 
            answer += ty[0]
    return answer

# ======================================
# Other's solution 


def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result