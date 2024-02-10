class Solution:
    def countSubstrings(self, s: str) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(start, end):
            nonlocal result
            if s[start:end+1] == s[start:end+1][::-1]:
                result +=1
            
            # loop with one less character
            if start < end:
                dfs(start + 1, end)
                dfs(start, end-1)
            
        result = 0
        dfs(0, len(s) - 1)
        return result