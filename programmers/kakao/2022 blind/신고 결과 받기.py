# First Trial
# Passed

def solution(id_list, report, k):
    answer = []
    reported = {}
    result = {}
    
    for id in id_list:
        reported[id] = 0
        result[id] = []
    
    report = set(report)
    for r in report:
        a, b = r.split()
        reported[b] += 1
        result[a].append(b)
        
    for id in result:
        cnt = 0
        for i in result[id]:
            if reported[i] >= k:
                cnt += 1
        answer.append(cnt)
    return answer


# Second Trial
# Passed

from collections import defaultdict

def solution(id_list, report, k):
    users = {}
    block = defaultdict(list)
    answer = [0] * len(id_list)
    # report = set(report)
    
    for idx, userID in enumerate(id_list):
        users[userID] = idx
    for r in report:
        userID, blockID = r.split(" ")
        if userID not in block[blockID]:
            block[blockID].append(userID)
    
    for blockID, userIDs in block.items():
        if len(userIDs) >= k:
            for userID in userIDs:
                answer[users[userID]] += 1
            
    return answer