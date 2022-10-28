class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # rolling hash idea
        d = defaultdict(list)
        # base needs to be a number greater than 26
        # since we only have lowercase letters so base > 26 would be enough
        base = 27
        M = 10**9+7
        
        # helper function to calculate the hashing value of a word
        def f(w):
            res = 0
            for c in w:
                res += pow(base, ord(c) - ord('a')) % M
            return res
        
        for w in strs:
            n = f(w)
            d[n].append(w)
        return list(d.values())