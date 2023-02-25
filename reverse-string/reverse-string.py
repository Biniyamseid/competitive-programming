class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        r = len(s)-1
        while i<r:
            s[i],s[r] = s[r],s[i]
            i+=1
            r-=1
        return s
        