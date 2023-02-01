class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        from collections import defaultdict
        tracker = defaultdict(int)
        for i in range(k):
            tracker[blocks[i]] += 1
        left = 0
        right = k
        minm = tracker["W"]
        while right < len(blocks):
            tracker[blocks[right]] += 1
            tracker[blocks[left]] -= 1
            right += 1
            left += 1
            minm = min(tracker["W"], minm)
        return minm if minm != float("inf") else len(blocks)


a = Solution()
print(a.minimumRecolors("BWWWBB", k=6))
