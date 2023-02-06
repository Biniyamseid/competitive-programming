class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            if w.startswith(pref):
                count += 1
        return count