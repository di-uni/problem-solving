# First Trial
# Test Failed (only case 1)

from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    cloth_dict = defaultdict(list)
    for cloth in clothes:
        cloth_dict[cloth[1]].append(cloth[0])
    # print(cloth_dict)
    for i in range(1, len(cloth_dict.keys()) + 1):
        # print(list(combinations(cloth_dict.keys(), i)))
        for categories in list(combinations(cloth_dict.keys(), i)):
            cnt = 1
            for c in categories:
                cnt *= len(cloth_dict[c])
            answer += cnt
            
        
    return answer


# Second Trial (referred to other's explanation)
# Test Passed

from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth_dict = defaultdict(list)
    for cloth in clothes:
        cloth_dict[cloth[1]].append(cloth[0])
    for c in cloth_dict.keys():
        # print(c, len(cloth_dict[c]))
        answer *= len(cloth_dict[c]) + 1


    return answer -1


# ==============================
# Other's Solution (1)

def solution(clothes):
    cloth_dict = {}
    
    for cloth in clothes:
        if cloth[1] not in cloth_dict:
            cloth_dict[cloth[1]] = 2
        else:
            cloth_dict[cloth[1]] += 1
    
    answer = 1
    for num in cloth_dict.values():
        answer *= num

    return answer -1


# ===================================
# Other's Solution (1)

import collections
from functools import reduce

def solution(c):
    return reduce(lambda x, y: x * y, [a+1 for a in collections.Counter([x[1] for x in c]).values()]) - 1