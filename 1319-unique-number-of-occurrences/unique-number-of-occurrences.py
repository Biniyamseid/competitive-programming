class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        keys = [x for y,x in count.items()]
        return len(keys)==len(set(keys))
        