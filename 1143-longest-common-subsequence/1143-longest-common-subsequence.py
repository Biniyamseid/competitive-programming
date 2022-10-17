class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp yisera
        dp = [[0 for _ in range(len(text2)+1)] for j in range(len(text1)+ 1)]
        print(dp)
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
                
        