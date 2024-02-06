class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        ans =[]
        groups = []
        for st in strs:
            s = sorted(st)
            if s in groups:
                ans[groups.index(s)].append(st)
            else:
                ans.append([st])
                groups.append(s)
        return ans