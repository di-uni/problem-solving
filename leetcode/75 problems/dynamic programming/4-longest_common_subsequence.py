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