# from collections import deque

# def solution(rc, operations):
#     answer = deque([])
#     for r in rc:
#         answer.append(deque(r))
#     w, h = len(answer[0]), len(answer)

#     temp = [0] * ((w + h) * 2 - 4)

#     for op in operations:
#         if op == "Rotate":
#             prev = answer[0][0]
#             for j in range(w-1):
#                 cur = answer[0][j + 1]
#                 answer[0][j + 1] = prev
#                 prev = cur
#             for i in range(1, h):
#                 cur = answer[i][w-1]
#                 answer[i][w-1] = prev
#                 prev = cur
#             for j in range(w-2, -1, -1):
#                 cur = answer[h-1][j]
#                 answer[h-1][j] = prev
#                 prev = cur
#             for i in range(h-2, -1, -1):
#                 cur = answer[i][0]
#                 answer[i][0] = prev
#                 prev = cur
#             # print(answer)
#         else:
#             answer.appendleft(answer.pop())
    
#     result = []
#     for r in answer:
#         result.append(list(r))
#     return result

# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))



# from collections import deque

# def solution(rc, operations):
#     answer = deque([])
#     for r in rc:
#         answer.append(deque(r))
#     w, h = len(answer[0]), len(answer)

#     temp = [0] * ((w + h) * 2 - 4)
#     rot_cnt = 0
#     prevRot = False

#     for op in operations:
#         if op == "Rotate":
#             if not prevRot:
#                 prevRot = True
#                 temp[:w] = list(answer[0])
#                 temp[w-1:w+h-1] = list(zip(*answer))[w-1]
#                 temp[w+h-2:2*w+h-2] = reversed(list(answer[h-1]))
#                 temp[2*w+h-3:2*(w+h)-3] = reversed(list(zip(*answer))[0])
#                 temp.pop()
#                 temp = deque(temp)
#             temp.appendleft(temp.pop())
#             print(temp)
#         else:
#             if prevRot:
#                 temp = list(temp)
#                 temp.append(temp[0])
#                 answer[0] = deque(temp[:w])
#                 for i in range(h):
#                     answer[i][w-1] = temp[w-1 + i]
#                     answer[h-1-i][0] = temp[2*w+h-3 + i]
#                 answer[h-1] = deque(reversed(temp[w+h-2:2*w+h-2]))
#                 # temp[w-1:w+h-1] = list(zip(*answer))[w-1]
#                 # temp[w+h-2:2*w+h-2] = reversed(list(answer[h-1]))
#                 # temp[2*w+h-3:2*(w+h)-3] = reversed(list(zip(*answer))[0])
                
#                 prevRot = False
#             answer.appendleft(answer.pop())
    
#     result = []
#     for r in answer:
#         result.append(list(r))
#     return result

from collections import deque

def solution(rc, operations):
    answer = deque([])
    for r in rc:
        answer.append(deque(r))
    w, h = len(answer[0]), len(answer)

    temp = [0] * ((w + h) * 2 - 4)
    rot_cnt = 0
    prevRot = False

    for idx, op in enumerate(operations):
        if op == "Rotate":
            if not prevRot:
                if idx < len(operations) - 1 and op[idx + 1] != "Rotate":
                    prev = answer[0][0]
                    for j in range(w-1):
                        cur = answer[0][j + 1]
                        answer[0][j + 1] = prev
                        prev = cur
                    for i in range(1, h):
                        cur = answer[i][w-1]
                        answer[i][w-1] = prev
                        prev = cur
                    for j in range(w-2, -1, -1):
                        cur = answer[h-1][j]
                        answer[h-1][j] = prev
                        prev = cur
                    for i in range(h-2, -1, -1):
                        cur = answer[i][0]
                        answer[i][0] = prev
                        prev = cur
                    continue
                else:
                    prevRot = True
                    temp[:w] = list(answer[0])
                    temp[w-1:w+h-1] = list(zip(*answer))[w-1]
                    temp[w+h-2:2*w+h-2] = reversed(list(answer[h-1]))
                    temp[2*w+h-3:2*(w+h)-3] = reversed(list(zip(*answer))[0])
                    temp.pop()
                    temp = deque(temp)
            temp.appendleft(temp.pop())
        else:
            if prevRot:
                temp = list(temp)
                temp.append(temp[0])
                answer[0] = deque(temp[:w])
                for i in range(h):
                    answer[i][w-1] = temp[w-1 + i]
                    answer[h-1-i][0] = temp[2*w+h-3 + i]
                answer[h-1] = deque(reversed(temp[w+h-2:2*w+h-2]))
                prevRot = False
            answer.appendleft(answer.pop())
    if prevRot:
        temp = list(temp)
        temp.append(temp[0])
        answer[0] = deque(temp[:w])
        for i in range(h):
            answer[i][w-1] = temp[w-1 + i]
            answer[h-1-i][0] = temp[2*w+h-3 + i]
        answer[h-1] = deque(reversed(temp[w+h-2:2*w+h-2]))
                
    result = []
    for r in answer:
        result.append(list(r))
    return result



print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
