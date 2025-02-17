class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l = 0
        traverse = False
        left = 0
 
        for i in range(0,len(s)):
            print(i,left)
            if i>0 and  s[i] == s[i-1]:
                l+=1
                if len(s[left:i+1]) == k:
                    if i<len(s)-1:
                        if s[i]!=s[i+1]:
                            return True
                    if i==len(s)-1:
                            return True
            elif i==0:
                if len(s[left:i+1]) == k:
                    if i<len(s)-1:
                        if s[i]!=s[i+1]:
                            return True
                    if i==len(s)-1:
                            return True


                # if l ==k-1:
                #     if i<len(s)-1:
                #         if s[i]!=s[i+1]:
                #             return True
                #     if i==len(s)-1:
                #         return True
            else:
                left=i
                l = 0
                if len(s[left:i+1]) == k:
                    if i<len(s)-1:
                        if s[i]!=s[i+1]:
                            return True
                    if i==len(s)-1:
                            return True
        return False


        