class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """needle == aaa"""
        """haystack == abccxfabc"""
        """lps = 012"""
        if needle == "":
            return 0
        def lpsconstructor(needle):
            lps = [0]*len(needle)
            prev = 0
            i = 1
            while i < len(needle):
                if needle[i] == needle[prev]:
                    lps[i] = prev + 1
                    i += 1
                    prev += 1
                elif prev == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev = lps[prev-1]
            return lps
        lps = lpsconstructor(needle)
        i = 0 #ptr for haystack
        j = 0 #ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i = i+1
                j = j+1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return i-len(needle)
        return -1
                    
                
            
        