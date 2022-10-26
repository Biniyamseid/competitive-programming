class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s == "":
            return True
        def generatelps(s):
            lps = [0]*len(s)
            prev = 0
            i = 1
            while i < len(s):
                if s[i] == s[prev]:
                    lps[i] = prev + 1
                    i += 1
                    prev += 1
                elif prev == 0:
                    lps[i] = 0
                    i+=1
                else:
                    prev = lps[prev-1]
            return lps
        
        lps = generatelps(s)
        print(lps)
        return lps[-1] and (lps[-1]%(len(s)-lps[-1])== 0)
            
        