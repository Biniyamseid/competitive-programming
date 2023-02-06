class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if self.isPredecessor(words[j], words[i]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        return ans

    def isPredecessor(self, word1, word2):
        if len(word1) + 1 != len(word2):
            return False
        i = 0
        for c in word2:
            if i == len(word1):
                return True
            if word1[i] == c:
                i += 1
        return i == len(word1)
