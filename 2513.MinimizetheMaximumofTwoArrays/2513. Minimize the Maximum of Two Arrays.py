class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l,  r = 0, 1 << 32 - 1

        lcm = math.lcm(divisor1, divisor2)

        def valid(num):
            div1 = num - num // divisor1
            if div1 < uniqueCnt1:

                return False
            div2 = num - num // divisor2
            if div2 < uniqueCnt2:

                return False
            union = num - num // lcm

            if union < (uniqueCnt1 + uniqueCnt2):

                return False
            return True

        while l + 1 != r:
            m = (l + r) // 2
            if (valid(m)):
                r = m
            else:
                l = m
        return r
