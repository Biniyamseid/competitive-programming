class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        while l<r and s[l]==s[r]:
            prev = l
            while l<r and s[l]==s[r]:
                l+=1
            while l<=r and s[prev]==s[r]:
                r-=1
        return r-l+1
        