class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        left = 0
        def check(left,right):
             if len(s[left:right+1]) == k:
                    if i<len(s)-1:
                        if s[right]!=s[right+1]:
                            return True
                    if right==len(s)-1:
                            return True
             return False


        for i in range(0,len(s)):
           
            if i>0 and  s[i] == s[i-1]:
                if check(left,i):return True
             
            elif i==0:
                if check(left,i):return True
            else:
                left=i
                if check(left,i):return True
        return False


        