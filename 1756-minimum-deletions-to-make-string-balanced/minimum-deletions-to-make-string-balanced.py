class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bcount = 0
        for l in s:
            if l == 'a':
                # either remove this 'a': res + 1
                # or keep this 'a': bcount (must remove all previous 'b's)
                res = min(res + 1, bcount)
            else:
                # Fine for 'b' in the tail
                bcount += 1
        return res