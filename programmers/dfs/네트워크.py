# # First Trial
# # Test Failed

# def solution(n, computers):
#     net = []

#     for i in range(n):
#         temp_net = -1
#         for n in range(len(net)):
#             if i in net[n]:
#                 temp_net = n
#         if temp_net == -1:
#             net.append([i])
#             temp_net = len(net) - 1

#         for idx, val in enumerate(computers[i]):
#             if val and idx not in net[temp_net]:
#                 net[temp_net].append(idx)

#     return len(net)


# # Second Trial
# # Test Failed

# def solution(n, computers):
#     net = []

#     for i in range(n):
#         isNew = True
#         temp = {i for i, v in enumerate(computers[i]) if v}
#         exist = -1
        
#         for n in range(len(net)):
#             if temp & net[n]:
#                 isNew = False
#                 net[n] |= temp
#                 # print(exist)
#                 if exist != -1:
#                     net[exist] |= net[n]
#                     del net[n]
#                 else:
#                     exist = n
#             # print(net)
#         if isNew:
#             net.append(temp)

#     return len(net)

n = 4
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
net = []

for i in range(n):
    isNew = True
    temp = {i for i, v in enumerate(computers[i]) if v}

    for n in range(len(net)):
        if temp & net[n]:
            isNew = False
            net[n] |= temp
    
    if isNew:
        net.append(temp)

print(net)
print(len(net))