# First Trial
# 정확성 Test Passed, 효율성 Test Failed

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    dict = defaultdict(list)
    
    for info_text in info:
        lan, field, exp, food, score = info_text.split(" ")
        tmp = [lan, field, exp, food]
        for num in range(5):
            for comb in list(combinations(tmp, num)):
                dict[tuple(comb)].append(int(score))
    
    # print(dict)
    
    for k in dict.keys():
        dict[k].sort()
        
    for q in query:
        q = q.split(" and ")
        score = q[-1].split(" ")
        q[-1], score = score[0], int(score[1])

        while '-' in q:
            q.remove('-')
                
        cnt = 0
        # print(q, dict[tuple(q)], score)
        for i in dict[tuple(q)]:
            if i >= score:
                cnt += 1
        answer.append(cnt)
            
    return answer

# ======================================
# Other's solution 
# Test Passed

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    dict = defaultdict(list)
    
    for info_text in info:
        lan, field, exp, food, score = info_text.split(" ")
        tmp = [lan, field, exp, food]
        for num in range(5):
            for comb in list(combinations(tmp, num)):
                dict[tuple(comb)].append(int(score))
    
    # print(dict)
    
    for k in dict.keys():
        dict[k].sort()
        
    for q in query:
        q = q.split(" and ")
        score = q[-1].split(" ")
        q[-1], score = score[0], int(score[1])

        while '-' in q:
            q.remove('-')
        
        qkey = tuple(q)

        if qkey in dict:  # query의 key가 info_dict의 key로 존재하면
            scores = dict[qkey]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, score)
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
            
    return answer