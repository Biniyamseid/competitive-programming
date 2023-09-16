class Solution:
        def checkStrings(self, s1: str, s2: str) -> bool:
            a1,b1 = s1[0::2], s1[1::2]
            a2,b2 = s2[0::2], s2[1::2]
            return sorted(a1)==sorted(a2) and sorted(b1)==sorted(b2)