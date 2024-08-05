class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        sets = set()
        s = set()
        order = 0
        for i in arr:
            if i  in s:
                sets.add(i)
            s.add(i)
           
        for i in arr:
            if i not in sets:
                order+=1
            if order ==k:
                return i
        return ""
        