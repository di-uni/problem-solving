# First Trial
# Test Passed

def solution(s):
    nums = {
        "zero": 0, 
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    answer = ""
    temp = ""
    
    for char in s:
        if char.isdigit():
            if temp:
                answer += str(nums[temp])
                temp = ""
            answer += char
        else:
            temp += char
            if temp in nums:
                answer += str(nums[temp])
                temp = ""
                
    
    return answer

print(solution("one4seveneight"))