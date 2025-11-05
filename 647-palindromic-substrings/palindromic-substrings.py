class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = r= i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                l-=1
                r+=1
            if i+1 <len(s) and s[i] == s[i+1]:
                l = i
                r=i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    count += 1
                    l-=1
                    r+=1

        return count
            

                # it is palindrome
        # start from end to present
        

        