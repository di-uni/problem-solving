# First Trial
# Test Passed

from collections import deque

def solution(begin, target, words):
    queue = deque([begin])
    queue_second = deque([])
    cnt = 0
    
    if target not in words:
        return 0
    
    while True:
        while queue:
            temp = queue.popleft()
            for word in words:
                diff = 0
                for t, w in zip(temp, word):
                    if t != w:
                        diff += 1
                if diff == 1:
                    queue_second.append(word)
                    if word == target:
                        return cnt + 1
        if queue_second:
            queue = queue_second
            queue_second = deque([])
        cnt += 1
            
    return 0



# Second Trial
# Re-write referred to Other's Solution 
# Test Passed

from collections import deque

def solution(begin, target, words):
    queue = deque([begin])
    cnt = 0
    
    if target not in words:
        return 0
    
    while True:
        temp_queue = deque([])
        while queue:
            temp = queue.popleft()
            for word in words:
                if sum([x != y for x, y in zip(temp, word)]) == 1:
                    temp_queue.append(word)
                    if word == target:
                        return cnt + 1
        if temp_queue:
            queue = temp_queue
        cnt += 1
            
    return 0



# ===================================
# Other's Solution
# Test Passed
# 속도가 훨씬 빠름

from collections import deque

def get_adjacent(current, words):
    for word in words:
        if sum([x != y for x, y in zip(current, word)]) == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])
    
    if target not in words:
        return 0
    
    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                if next_word == target:
                    return dist[current] + 1
                dist[next_word] = dist[current] + 1
                queue.append(next_word)
            
    return 0