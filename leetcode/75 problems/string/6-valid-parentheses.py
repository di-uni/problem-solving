# 2022.09.29
# First Trial
# Test Passed 
# Runtime: faster than 10.69%, Memory Usage: less than 72.33%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for e in s:
            if e == '(':
                stack.append(')')
            elif e == '{':
                stack.append('}')
            elif e == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != e:
                    return False
        
        if stack:
            return False
        
        return True



# =================================================================
# Other's Solution
# Using hash
# Runtime: faster than 23.38%, Memory Usage: less than 72.33%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "}": "{", "]": "["}
        
        for e in s:
            if e in dict.values():
                stack.append(e)
            if e in dict.keys():
                if not stack or stack.pop() != dict[e]:
                    return False
            
        return stack == []
            