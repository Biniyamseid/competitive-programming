class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        keys = [x for x in count.values()]
        return len(keys)==len(set(keys))
        