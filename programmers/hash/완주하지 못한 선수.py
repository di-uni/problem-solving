# First Trial
# Test Passed

def solution(participant, completion):
    answer = ''
    hash = {}

    for c_name in completion:
        if c_name not in hash:
            hash[c_name] = 0
        hash[c_name] += 1

    for p_name in participant:
        if p_name not in hash or hash[p_name] == 0:
            answer = p_name
            break
        hash[p_name] -= 1

    return answer


# ==============================
# Other's Solution (1)
# use hash function

import collections

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


# Other's Solution (2)
# use Counter

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]