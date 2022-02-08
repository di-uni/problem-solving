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