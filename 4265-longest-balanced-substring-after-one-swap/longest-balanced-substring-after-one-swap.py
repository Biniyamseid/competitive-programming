from collections import defaultdict
from bisect import bisect_left

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        totalones = s.count("1")
        totalzeros = n - totalones

        pref = 0
        positions = defaultdict(list)
        positions[0].append(-1)   # prefix sum 0 before the string starts

        first = {0: -1}           # earliest occurrence for balanced case
        res = 0

        for idx, ch in enumerate(s):
            pref += 1 if ch == "1" else -1

            # sum = 0
            if pref in first:
                res = max(res, idx - first[pref])
            else:
                first[pref] = idx

            # sum = +2
            # length must be <= 2 * totalzeros
            target = pref - 2
            if target in positions:
                min_j = idx - 2 * totalzeros
                k = bisect_left(positions[target], min_j)
                if k < len(positions[target]):
                    j = positions[target][k]
                    res = max(res, idx - j)

            # sum = -2
            # length must be <= 2 * totalones
            target = pref + 2
            if target in positions:
                min_j = idx - 2 * totalones
                k = bisect_left(positions[target], min_j)
                if k < len(positions[target]):
                    j = positions[target][k]
                    res = max(res, idx - j)

            positions[pref].append(idx)

        return res