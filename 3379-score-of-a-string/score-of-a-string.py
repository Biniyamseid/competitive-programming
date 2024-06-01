class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        prev = 0
        for i in s:
            if prev ==0:
                pass
            else:
                ans += abs(int(ord(i))-int(prev))
            
            prev = ord(i)
            


        return ans
        