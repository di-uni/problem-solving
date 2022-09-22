def solution(board, aloc, bloc):
    answer = -1
    height = len(board)
    width = len(board[0])
    
    def dfs(i, A, B, curr_board, temp):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        if i % 2 == 0:
            nextEmpty = True
            for k in range(4):
                Any = A[0] + dx[k]
                Anx = A[1] + dy[k]

                if 0 <= Anx < width and 0 <= Any < height and curr_board[Any][Anx]:
                    curr_board[A[0]][A[1]] = 0
                    dfs(i+1, [Any, Anx], B, curr_board, temp)
                    curr_board[A[0]][A[1]] = 1
                    nextEmpty = False
            if nextEmpty:
                print(i,temp)
                
                temp.append(i)
                # min_val = min(min_val, i)
                # return i
                return temp
                        
        else:
            nextEmpty = True
            for k in range(4):
                Bny = B[0] + dx[k]
                Bnx = B[1] + dy[k]
                
                if 0 <= Bnx < width and 0 <= Bny < height and curr_board[Bny][Bnx]:
                    nextEmpty = False
                    curr_board[B[0]][B[1]] = 0
                    dfs(i+1, A, [Bny, Bnx], curr_board, temp)
                    curr_board[B[0]][B[1]] = 1
            if nextEmpty:
                # min_val = min(min_val, i)
                print(i, temp)
                temp.append(i)
                # return i
                return temp
                       
    p = dfs(0, aloc, bloc, board, [])
    print(p)
    return answer


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]))
