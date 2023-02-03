class Solution:
    def validPalindrome(self, s: str) -> bool:
        # construct a method with s and able, able tells us is it able or not to chang eone character des yemilew neger we have only two options either go to left or right
        def validator(l, r, able):
            if r >= len(s) or l >= len(s):
                return True
            if r-l <= 0:
                return True
            if s[l] == s[r]:
                return validator(l+1, r-1, able)
            else:
                if able:
                    return validator(l, r-1, False) or validator(l+1, r, False)
                else:
                    return False
        return validator(0, len(s)-1, True)
