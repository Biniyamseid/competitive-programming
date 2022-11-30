class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        vals = set(arr)
        counts = set()
        for i in count.values():
            counts.add(i)
        return len(counts) == len(vals)
        