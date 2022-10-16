# 2022.10.16
# First trial
# Test Passed
# Runtime: faster than 67.57%, Memory Usage: less than 7.05%

from collections import Counter, defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_dict = defaultdict(int)
        guess_dict = defaultdict(int)
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_dict[s] += 1
                guess_dict[g] += 1
                
        # print(secret_dict, guess_dict)
        
        for key, val in secret_dict.items():
            if key in guess_dict:
                cows += min(val, guess_dict[key])
                
        return f"{bulls}A{cows}B"


# =================================================================
# Other's Solution
# Shortest
# Runtime: faster than 51.15%, Memory Usage: less than 32.78% 

from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        bulls = sum(i == j for i, j in zip(secret, guess))
        # s & g : s와 g의 교집합
        return '%sA%sB' % (bulls, sum((s & g).values()) - bulls)