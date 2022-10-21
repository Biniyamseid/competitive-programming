class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp yisera
        dp = [[0 for _ in range(len(text1)+1)]for _ in range(len(text2)+1)]
        #print(dp)
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #print(dp)
        #print(dp[len(text2)-1][len(text1)-1])
        return dp[len(text2)-1][len(text1)-1]
                
        