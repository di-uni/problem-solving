# First Trial
# Test Failed

# def solution(tickets):
    
#     def dfs(array):
#         if len(array) == len(tickets) + 1:
#             new_array = array[:]
#             print(array)
#             return new_array
#             # yield new_array
#         else:
#             for dep, des in tickets:
#                 if dep == array[-1]:
#                     array.append(des)
#                     dfs(array)
#                     array.pop()
#                     print(array)
#             return array

#     answer = ["ICN"]
#     hey = dfs(answer)
#     # for solution in dfs(answer):
#     #     print(solution)
#     return hey

# print("answer:", solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# # solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])




# def solution(tickets):
#     answer = ["ICN"]
#     visited = {"ICN": True}
    
#     while len(answer) < len(tickets) + 1:
#         for dep, des in tickets:
#             if dep == answer[-1] and des not in visited:
#                 answer.append(des)
#                 visited[des] = True
#                 print(answer)
#                 break
            
#     return answer



# ======================================
# Other's solution 
# Test Passed

from collections import defaultdict
def solution(tickets):
    path = []

    # 1. {시작점: [도착점리스트]} 형태로 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 2. 도착점 리스트를 역순 정렬
    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    # 3. 출발지는 항상 ICN이므로 stack에 먼저 넣어두기
    stack = ["ICN"]
    # 4. DFS로 모든 노드 순회
    while stack:
        # 4-1. 스택에서 가장 위의 저장된 데이터 꺼내오기
        top = stack.pop()

        # 4-2. top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or not graph[top]:
            path.append(top)
        # 4-3. top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(graph[top].pop())
        # print("\npath: ", path, "\nstack: ", stack)

    # 5. path를 뒤집어서 반환
    return path[::-1]