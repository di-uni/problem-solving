from itertools import combinations 
from collections import defaultdict

def solution(orders, course):
    answer = []
    course_dict = defaultdict(int)
    
    for num in course:
        for order in orders:
            if len(order) < num:
                continue
            alpha_order = ''.join(sorted(order))
            for menu in list(combinations(alpha_order, num)):
                course_dict[''.join(menu)] += 1
        # print(course_dict)
        if course_dict:
            max_value = max(course_dict.values())
            if max_value > 1:
                answer += [key for key, value in course_dict.items() if value == max_value]
                # print(answer)
        course_dict = defaultdict(int)
         
        
    return sorted(answer)


# 개선
from itertools import combinations 
from collections import defaultdict

def solution(orders, course):
    answer = []
    course_dict = defaultdict(int)
    
    for num in course:
        for order in orders:
            if len(order) < num:
                continue
            for menu in list(combinations(sorted(order), num)):
                course_dict[''.join(menu)] += 1
        if course_dict:
            max_value = max(course_dict.values())
            if max_value > 1:
                answer += [key for key, value in course_dict.items() if value == max_value]
        course_dict = defaultdict(int)
         
        
    return sorted(answer)



# ======================================
# Other's solution 


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]