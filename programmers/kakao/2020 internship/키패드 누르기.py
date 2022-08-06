# First Trial
# Test Passed

def solution(numbers, hand):
    answer = ''
    # keypad = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     ['*', 0, '#'],
    # ]
    left, right = [3, 0], [3, 2]
    
    for n in numbers:
        coord = [(n - 1) // 3, (n - 1) % 3]
        isLeft, isRight = False, False
        
        if n % 3 == 1:
            isLeft = True
        elif n != 0 and n % 3 == 0:
            isRight = True
        else:
            if n == 0:
                coord = [3, 1]
            left_dist = abs(coord[0] - left[0]) + abs(coord[1] - left[1])
            right_dist = abs(coord[0] - right[0]) + abs(coord[1] - right[1])
            # print(n, left_dist, right_dist, left, right)
            if left_dist == right_dist:
                if hand == "left":
                    isLeft = True
                else:
                    isRight = True
            elif left_dist < right_dist:
                isLeft = True
            else:
                isRight = True
                
        if isLeft:
            answer += 'L'
            left = coord
        elif isRight:
            answer += "R"
            right = coord
            
    return answer



# Second Trial referred to Other's Solution
# Test Passed

def solution(numbers, hand):
    answer = ''
    keypad = { 
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2],
    }
        
    left, right = keypad['*'], keypad['#']
    
    for n in numbers:
        coord = keypad[n]
        isLeft, isRight = False, False
        
        if n % 3 == 1:
            isLeft = True
        elif n != 0 and n % 3 == 0:
            isRight = True
        else:
            left_dist = abs(coord[0] - left[0]) + abs(coord[1] - left[1])
            right_dist = abs(coord[0] - right[0]) + abs(coord[1] - right[1])
            # print(n, left_dist, right_dist, left, right)
            if left_dist == right_dist:
                if hand == "left":
                    isLeft = True
                else:
                    isRight = True
            elif left_dist < right_dist:
                isLeft = True
            else:
                isRight = True
                
        if isLeft:
            answer += 'L'
            left = coord
        elif isRight:
            answer += "R"
            right = coord
            
    return answer