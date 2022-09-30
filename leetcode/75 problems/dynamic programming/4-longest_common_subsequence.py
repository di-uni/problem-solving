class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        n, m = len(text1), len(text2)
        dp = [[None] * n for x in range(m)]
        
        def subsequence(i, j):
            if i >= 0 and j >= 0:
                # if dp[i][j] != None:
                if i == 0 and j == 0:
                    if text1[i] == text2[j]:
                        return 1
                    else:
                        return 0
                if text1[i] == text2[j]:
                    print(text1[i], text2[j])
                    return subsequence(i-1, j-1) + 1
                else:
                    return max(subsequence(i-1, j), subsequence(i, j-1))
        
        
        return subsequence(n-1, m-1)


        n, m = len(text1), len(text2)
        dp = [[None] * m for x in range(n)]
        
        def subsequence(i, j):
            # print(i, j, text1[i], text2[j])
            if dp[i][j] == None:
                if i == 0 and j == 0:
                    # print("1")
                    if text1[i] == text2[j]:
                        return 1
                    else:
                        return 0
                else:
                    if text1[i] == text2[j]:
                        # print("2")
                        temp_i, temp_j = 0, 0
                        if i > 0: temp_i = i - 1
                        if j > 0: temp_j = j - 1  
                        # dp[i][j] = subsequence(i-1, j-1) + 1
                        dp[i][j] = subsequence(temp_i, temp_j) + 1
                        # print("2", i, j, text1[i], text2[j], dp[i][j])
                    else:
                        # print("3")
                        temp_i, temp_j = 0, 0
                        if i > 0: temp_i = i - 1
                        if j > 0: temp_j = j - 1  
                        if i == 0:
                            if j > 1:
                                dp[i][j] = max(subsequence(i, j - 1), subsequence(i, j - 2))
                            else:
                                dp[i][j] = subsequence(0, 0)
                        elif j == 0:
                            if i > 1:
                                dp[i][j] = max(subsequence(i - 1, j), subsequence(i - 2, j))
                            else:
                                dp[i][j] = subsequence(0, 0)
                        else:
                            dp[i][j] = max(subsequence(temp_i, j), subsequence(i, temp_j))
                        # print("3", i, j, text1[i], text2[j], dp[i][j])

            return dp[i][j]
        
        return subsequence(n-1, m-1)


# 2022.09.30
# First Trial
# Time Limit Exceeded

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_common = 0
        short, long = text1, text2
        if len(text2) < len(text1):
            short, long = text2, text1
        # print(short, long)
        dp = [[0]*(len(short)) for _ in range(len(long))]
        
        # print(dp)
        
        for i in range(len(short)):
            for j in range(len(long)):
                if short[i] == long[j]:
                    # print("j, i: ", j, i)
                    dp[j][i] += 1
                    max_common = max(max_common, dp[j][i])
                    for x in range(i+1, len(short)):
                        for y in range(j+1, len(long)):
                            dp[y][x] = max(dp[y][x], dp[j][i])
                    # print(dp)
                    # break
        # print(dp)
        
        return max_common


# =================================================================
# Other's Solution
# Using dp
# https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis

# Runtime: faster than 40.44%, Memory Usage: less than 79.26%

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
    
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i+1][j+1] = dp[i][j] + 1 if c == d else max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]