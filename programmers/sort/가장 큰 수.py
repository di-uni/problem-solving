# First Trial
# 시간 초과

def solution(numbers):
    answer = ''
    nums = [str(n) for n in numbers]
    nums.sort()
    # nums.sort(reverse="True")
    
    # print(nums)
    
    for i in range(1, len(numbers)):
        # print(nums, nums[i - 1], nums[i])
        if nums[i - 1][0] == nums[i][0]:
            if len(nums[i-1]) == len(nums[i]):
                a = nums[i-1][-1]
                b = nums[i][-1]
            else:
                l = min(len(nums[i-1]), len(nums[i]))
                if len(nums[i-1]) == l:
                    a = nums[i-1][0]
                    b = nums[i][l]
                else:
                    a = nums[i-1][l]
                    b = nums[i][0]
                if a > b:   # swiping
                    temp = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = temp
            
    # print(nums)
    for i in range(len(numbers) - 1, -1, -1):
        if answer == "0" and nums[i] == "0":
            return "0"
        answer += nums[i]
        
    return answer



# =========================
# Other's solution

# 각 문자에 *3을 한다는 것은 다음과 같은 의미를 가진다.

# ex1) 21 + 212 = 21212 < 212 + 21 = 21221 의 비교에서, 
# 212121 , 212212212 두 숫자를 비교했을 때 오른쪽이 크므로, 212가 선행해야 한다.
# ex2) 12 + 121 = 12121 > 121 + 12 = 12112 의 비교에서,
# 121212 , 121121121 두 숫자를 비교했을 때 왼쪽이 크므로, 12가 선행해야 한다.
# ex3) 1 + 10 = 110 > 10 + 1 = 101 의 비교에서,
# 111, 101010 두 숫자를 비교했을 때 왼쪽이 크므로, 1이 선행해야 한다.

# 즉, 핵심이 되는 자리 수가 다를 때의 비교가 가능한 모양을 
# str*3을 통해 간접적으로 만들어줌으로써 그들간의 비교 연산을 진행하는 것만으로 정렬을 마칠 수 있다. 
# (자기 자신을 반복해서 붙였을 때 큰 숫자가 앞에 와야함)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))   # [0,0,0] 등 케이스 처리를 위해 int로 변환