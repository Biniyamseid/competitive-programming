class Solution:
    def maximum69Number (self, num: int) -> int:
        l = 0
        s = list(str(num))
        while l < len(s):
            if s[l] == "6":
                s[l] = "9"
                break
            l+=1
        return "".join(s)
        
        