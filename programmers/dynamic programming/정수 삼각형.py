# First Trial
# Test Passed

def solution(triangle):
    prev = [] 
    cur = []
    
    prev.append(triangle[0][0])
    h = 1
    while h < len(triangle):
        cur = []
        cur.append(prev[0] + triangle[h][0])
        for i in range(1, len(prev)):
            cur.append(max(prev[i - 1], prev[i]) + triangle[h][i])
        cur.append(prev[len(prev) - 1] + triangle[h][len(prev)])
        prev = cur
        h += 1

    return max(cur)


# ==============================
# Other's Solution

def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer


