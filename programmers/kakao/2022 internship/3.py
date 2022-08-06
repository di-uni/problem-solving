# import sys
# sys.setrecursionlimit(10**6)

# def solution(alp, cop, problems):
#     answer = 0

#     problems.sort(key=lambda x : (x[0], x[1]))
#     print(problems)
#     canSolve = []

#     def dp(need_alp, need_cop, _alp_req, _cop_req, _cost, _time, basis):
#         if _time > basis:
#             return (_time, need_alp, need_cop)
#         if need_alp <= 0 and need_cop <= 0:
#             # print(_time)
#             return (_time, need_alp, need_cop)
#         return min(
#         dp(need_alp-1, need_cop, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp, need_cop-1, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp-_alp_req, need_cop-_cop_req, _alp_req, _cop_req, _cost, _time+_cost, basis),
#         key= lambda x : x[0])



#     alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[0]
#     if alp < alp_req:
#         answer += alp_req - alp
#         alp = alp_req
#     if cop < cop_req:
#         answer += cop_req - cop
#         cop = cop_req
#     canSolve.append([alp_rwd, cop_rwd, cost])

#     alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[1]
#     prev_alp_rwd, prev_cop_rwd, prev_cost = canSolve[0]
#     if alp < alp_req or cop < cop_req:
#         temp1 = alp_req - alp + cop_req - cop
#         temp2, need_alp, need_cop = dp(alp_req-alp, cop_req-cop, prev_alp_rwd, prev_cop_rwd, prev_cost, 0, temp1)
#         print(temp1, temp2, need_alp, need_cop)
#         if temp1 >= temp2:
#             alp = alp_req
#             cop = cop_req
#         else:
#             alp = alp_req - need_alp
#             cop = cop_req - need_cop
#         answer += min(temp1, temp2)


    


#     return answer


# import sys
# sys.setrecursionlimit(10**6)

# def solution(alp, cop, problems):
#     answer = 0

#     problems.sort(key=lambda x : (x[0], x[1]))
#     max_alp = max(problems, key=lambda x : x[0])
#     max_cop = max(problems, key=lambda x : x[1])

#     visited = [False] * len(problems)
#     canSolve = []

#     def dp(need_alp, need_cop, _alp_req, _cop_req, _cost, _time, basis):
#         if _time > basis:
#             return (_time, need_alp, need_cop)
#         if need_alp <= 0 and need_cop <= 0:
#             return (_time, need_alp, need_cop)
#         return min(
#         dp(need_alp-1, need_cop, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp, need_cop-1, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp-_alp_req, need_cop-_cop_req, _alp_req, _cop_req, _cost, _time+_cost, basis),
#         key= lambda x : x[0])

#     def dp2(need_alp, need_cop, _alp_req, _cop_req, _cost, _time, basis):
#         if _time > basis:
#             return (_time, need_alp, need_cop)
#         if need_alp <= 0 and need_cop <= 0:
#             return (_time, need_alp, need_cop)
#         return min(
#         dp(need_alp-1, need_cop, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp, need_cop-1, _alp_req, _cop_req, _cost, _time+1, basis),
#         dp(need_alp-_alp_req, need_cop-_cop_req, _alp_req, _cop_req, _cost, _time+_cost, basis),
#         key= lambda x : x[0])

#     def check(i, alp, cop, time):
#         print(i, visited, alp, cop)
#         visited[i] = True
#         checkList = []

#         if not (False in visited):
#             print("return:", time)
#             return time

#         if alp >= max_alp and cop >= max_cop:
#             return time

#         for i in range(len(visited)):
#             if visited[i] == False:
#                 alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
#                 if alp < alp_req or cop < cop_req: 
#                     checkList.append(i)
#                 else:
#                     visited[i] = True
#                     canSolve.append(problems[i])
        
#         next_i, next_alp, next_cop = -1, 0, 0
#         tmp_time = float("inf")
#         print(checkList)

#         for i in checkList:
#             print(i, " checkList: ", problems[i], alp, cop)
#             alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
#             simple_study = alp_req - alp + cop_req - cop
#             solve_study = float("inf")
#             need_alp, need_cop = float("inf"), float("inf")

#             for solved in canSolve:
#                 a, c, prev_alp_rwd, prev_cop_rwd, prev_cost = solved
#                 temp, temp_need_alp, temp_need_cop = dp(alp_req-alp, cop_req-cop, prev_alp_rwd, prev_cop_rwd, prev_cost, 0, simple_study)
#                 solve_study = min(solve_study, temp)
#                 if solve_study == temp:
#                     need_alp = min(need_alp, temp_need_alp)
#                     need_cop = min(need_cop, temp_need_cop)
#             if tmp_time > min(simple_study, solve_study):
#                 if simple_study >= solve_study:
#                     next_alp = alp_req
#                     next_cop = cop_req
#                 else:
#                     next_alp = alp_req - need_alp
#                     next_cop = cop_req - need_cop
#                 next_i = i
#                 tmp_time = min(simple_study, solve_study)
#             print(tmp_time, simple_study, solve_study, need_alp, need_cop)

#         print("next i: ", next_i, next_alp, next_cop, tmp_time)
#         time += tmp_time
#         canSolve.append(problems[next_i])
#         return check(next_i, next_alp, next_cop, time)
#         # return time
        

#     alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[0]
#     if alp < alp_req:
#         answer += alp_req - alp
#         alp = alp_req
#     if cop < cop_req:
#         answer += cop_req - cop
#         cop = cop_req
#     canSolve.append(problems[0])
#     visited[0] = True


#     answer += check(0, alp, cop, 0)

#     # for p in problems:
#     #     print(p, alp, cop)
#     #     alp_req, cop_req, alp_rwd, cop_rwd, cost = p
#     #     if alp < alp_req or cop < cop_req:
#     #         simple_study = alp_req - alp + cop_req - cop
#     #         solve_study = float("inf")
#     #         need_alp, need_cop = float("inf"), float("inf")
#     #         for solved in canSolve:
#     #             prev_alp_rwd, prev_cop_rwd, prev_cost = solved
#     #             temp, temp_need_alp, temp_need_cop = dp(alp_req-alp, cop_req-cop, prev_alp_rwd, prev_cop_rwd, prev_cost, 0, simple_study)
#     #             solve_study = min(solve_study, temp)
#     #             if solve_study == temp:
#     #                 need_alp = min(need_alp, temp_need_alp)
#     #                 need_cop = min(need_cop, temp_need_cop)
#     #         print(simple_study, solve_study, need_alp, need_cop)
#     #         if simple_study >= solve_study:
#     #             alp = alp_req
#     #             cop = cop_req
#     #         else:
#     #             alp = alp_req - need_alp
#     #             cop = cop_req - need_cop
#     #         answer += min(simple_study, solve_study)
#     #     canSolve.append([alp_rwd, cop_rwd, cost])


    


#     return answer


# import sys
# sys.setrecursionlimit(10**6)

# def solution(alp, cop, problems):
#     answer = 0

#     problems.sort(key=lambda x : (x[0] + x[1]))
#     visited = [False] * len(problems)
#     canSolve = []

#     # def dp(need_alp, need_cop, _alp_req, _cop_req, _cost, _time, basis):
#     def dp(alp, cop, need_alp, need_cop, canSolve, _time, basis):
#         if False in visited:
#             for i in range(len(visited)):
#                 if visited[i] == False:
#                     p = problems[i]
#                     if alp >= p[0] and cop >= p[1]:
#                         canSolve.append(p)
#                         visited[i] = True
#         if _time > basis:
#             return (_time, need_alp, need_cop)
#         if need_alp <= 0 and need_cop <= 0:
#             return (_time, need_alp, need_cop)
#         return min(
#             # dp(need_alp-1, need_cop, _alp_req, _cop_req, _cost, _time+1, basis),
#             # dp(need_alp, need_cop-1, _alp_req, _cop_req, _cost, _time+1, basis),
#             # dp(need_alp-_alp_req, need_cop-_cop_req, _alp_req, _cop_req, _cost, _time+_cost, basis),
#             dp(alp, cop, need_alp-1, need_cop, canSolve, _time+1, basis),
#             dp(alp, cop, need_alp, need_cop-1, canSolve, _time+1, basis),
#             yieldDp(alp, cop, need_alp, need_cop, canSolve, _time, basis),
#             key= lambda x : x[0])
    
#     def yieldDp(alp, cop, need_alp, need_cop, canSolve, _time, basis):
#         for a, b, _alp_req, _cop_req, _cost in canSolve:
#             yield dp(alp, cop, need_alp-_alp_req, need_cop-_cop_req, canSolve, _time+_cost, basis)

#     def check(i, alp, cop, time):
#         visited[i] = True
#         checkList = []

#         if not (False in visited):
#             print(time)
#             return time

#         for i in range(len(visited)):
#             if visited[i] == False:
#                 alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
#                 if alp < alp_req or cop < cop_req: 
#                     checkList.append(i)
#                 else:
#                     visited[i] = True
#                     canSolve.append(problems[i])
        
#         next_i, next_alp, next_cop = -1, 0, 0
#         tmp_time = float("inf")

#         for i in checkList:
#             print(problems[i], alp, cop)
#             alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
#             simple_study = alp_req - alp + cop_req - cop
#             solve_study = float("inf")
#             need_alp, need_cop = float("inf"), float("inf")

#             for solved in canSolve:
#                 a, c, prev_alp_rwd, prev_cop_rwd, prev_cost = solved
#                 temp, temp_need_alp, temp_need_cop = dp(alp_req-alp, cop_req-cop, prev_alp_rwd, prev_cop_rwd, prev_cost, 0, simple_study)
#                 solve_study = min(solve_study, temp)
#                 if solve_study == temp:
#                     need_alp = min(need_alp, temp_need_alp)
#                     need_cop = min(need_cop, temp_need_cop)
#             print(simple_study, solve_study, need_alp, need_cop)
#             if tmp_time > min(simple_study, solve_study):
#                 if simple_study >= solve_study:
#                     next_alp = alp_req
#                     next_cop = cop_req
#                 else:
#                     next_alp = alp_req - need_alp
#                     next_cop = cop_req - need_cop
#                 next_i = i
#             tmp_time = min(simple_study, solve_study)

#         time += tmp_time
#         canSolve.append(problems[next_i])
#         check(next_i, next_alp, next_cop, time)
#         return time
        

#     # first 
#     alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[0]
#     if alp < alp_req:
#         answer += alp_req - alp
#         alp = alp_req
#     if cop < cop_req:
#         answer += cop_req - cop
#         cop = cop_req
#     for idx, p in enumerate(problems):
#         if alp >= p[0] and cop >= p[1]:
#             canSolve.append(p)
#             visited[idx] = True

#     answer += check(0, alp, cop, 0)

#     return answer


import sys
sys.setrecursionlimit(10**6)

def solution(alp, cop, problems):
    answer = 0

    problems.sort(key=lambda x : (x[0] + x[1]))
    visited = [False] * len(problems)
    max_alp = max(problems, key=lambda x : x[0])[0]
    max_cop = max(problems, key=lambda x : x[1])[1]
    canSolve = []

    # def dp(need_alp, need_cop, _alp_req, _cop_req, _cost, _time, basis):
    def dp(alp, cop, need_alp, need_cop, canSolve, _time, basis):
        
        if _time > basis:
            return (_time, need_alp, need_cop)
        if need_alp <= 0 and need_cop <= 0:
            return (_time, need_alp, need_cop)
        if alp >= max_alp and cop >= max_cop:
            return (_time, need_alp, need_cop)
        
        if False in visited:
            for i in range(len(visited)):
                if visited[i] == False:
                    p = problems[i]
                    if alp >= p[0] and cop >= p[1]:
                        canSolve.append(p)
                        visited[i] = True

        # print(visited, canSolve)
        tmp_list = []
        for a,b, alp_req, cop_req, cost in canSolve:
            tmp_list.append(dp(alp+alp_req, cop+cop_req, need_alp-alp_req, need_cop-cop_req, canSolve, _time+cost, basis))

        tmp_list.append(dp(alp+1, cop, need_alp-1, need_cop, canSolve, _time+1, basis))
        tmp_list.append(dp(alp, cop+1, need_alp, need_cop-1, canSolve, _time+1, basis))
        return min(
            tmp_list,
            key= lambda x : x[0])
        
    
    def check(i, alp, cop, time):
        visited[i] = True
        checkList = []

        if alp >= max_alp and cop >= max_cop:
            return time

        if not (False in visited):
            # print(time)
            return time
        
        if False in visited:
            for i in range(len(visited)):
                if visited[i] == False:
                    alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
                    if alp < alp_req or cop < cop_req: 
                        checkList.append(i)
                    else:
                        visited[i] = True
                        canSolve.append(problems[i])
        
        next_i, next_alp, next_cop = -1, 0, 0
        tmp_time = float("inf")

        for i in checkList:
            # print(problems[i], alp, cop)
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
            simple_study = alp_req - alp + cop_req - cop
            solve_study, need_alp, need_cop = dp(alp, cop, alp_req-alp, cop_req-cop, canSolve, 0, simple_study)
            if tmp_time > min(simple_study, solve_study):
                if simple_study >= solve_study:
                    next_alp = alp_req
                    next_cop = cop_req
                else:
                    next_alp = alp_req - need_alp
                    next_cop = cop_req - need_cop
                next_i = i
            tmp_time = min(simple_study, solve_study)

        time += tmp_time
        canSolve.append(problems[next_i])
        visited[next_i] = True
        check(next_i, next_alp, next_cop, time)
        return time
        

    # first 
    alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[0]
    if alp < alp_req:
        answer += alp_req - alp
        alp = alp_req
    if cop < cop_req:
        answer += cop_req - cop
        cop = cop_req
    for idx, p in enumerate(problems):
        if alp >= p[0] and cop >= p[1]:
            canSolve.append(p)
            visited[idx] = True

    answer += check(0, alp, cop, 0)

    return answer


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))