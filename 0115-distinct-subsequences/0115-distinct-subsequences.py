class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(r,c):
            if c>= len(t):
                return 1
            if r>= len(s):
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            if s[r] == t[c]:
                cache[(r,c)] = dfs(r+1,c+1) + dfs(r+1,c)
            else:
                cache[(r,c)] = dfs(r+1,c)
            return cache[(r,c)]
        return dfs(0,0)
        