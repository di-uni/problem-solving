def solution(array, commands):
    answer = []
    
    # print(array)
    for command in commands:
        temp = array[command[0] - 1:command[1]]
        # print(temp)
        temp.sort()
        answer.append(temp[command[2] - 1])
        
    return answer