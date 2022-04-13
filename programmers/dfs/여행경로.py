
def solution(tickets):
    
    def dfs(array):
        if len(array) == len(tickets) + 1:
            new_array = array[:]
            print(array)
            return new_array
            # yield new_array
        else:
            for dep, des in tickets:
                if dep == array[-1]:
                    array.append(des)
                    dfs(array)
                    array.pop()
                    print(array)
            return array

    answer = ["ICN"]
    hey = dfs(answer)
    # for solution in dfs(answer):
    #     print(solution)
    return hey

print("answer:", solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])