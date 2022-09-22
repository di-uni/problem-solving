# First Trial
# Test Failed

from collections import defaultdict
from itertools import combinations

def solution(relation):
    answer = 0
    cols = len(relation[0])
    data = defaultdict(list)
    keys = set([])

    for i in range(len(relation)):
        for j in range(cols):
            data[j].append(relation[i][j])

    for i in range(1, cols + 1):
        if len(data.keys()) < i:
            break
        for comb in list(combinations(data.keys(), i)):
            tmp = []
            values = list(map(lambda x: data[x], comb))
            for j in range(len(values[0])):
                pair = []
                for k in range(len(values)):
                    pair.append(values[k][j])
                tmp.append(tuple(pair))
            # print(tmp)
            if len(tmp) == len(set(tmp)):
                for k in comb:
                    keys.add(k)
                answer += 1

        for key in keys:
            del data[key]
        keys = set([])

    return answer



# ======================================
# Other's solution 
# Test Passed

from collections import defaultdict
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    combis = []
    for i in range(1, col + 1):
        combis += list(combinations(range(col), i))
    
    unique = []
    for combi in combis:
        # tmp = []
        # for r in range(row):
        #     val = []
        #     for c in combi:
        #         val.append(relation[r][c])
        #     tmp.append(' '.join(val))
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        if len(set(tmp)) == row:
            for x in unique:
                if set(x).issubset(set(combi)):
                    break
            else:
                unique.append(combi)

    return len(unique)
