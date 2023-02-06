class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {word:1 for word in words}
        ans = 0
        def bottom(word):
            ans = 1
            for i in range(len(word)):
                pred = word[:i]+word[i+1:]
                if pred in dp:
                    dp[word] = max(dp[word],dp[pred]+1)
                ans = max(ans,dp[word])
            return ans
        return max([bottom(word) for word in dp])
        
        
