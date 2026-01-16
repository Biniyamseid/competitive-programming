class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # find maximum common value in both parts
        hFences.extend([1,m])
        vFences.extend([1,n])
        a = hFences
        b = vFences
        a.sort()
        b.sort()
        print(a)
        print(b)

        i, j = 0, len(a) - 1
        x, y = 0, len(b) - 1

        diffs_a = set()
        diffs_b = set()
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                diffs_a.add(hFences[j]-hFences[i])
        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                diffs_b.add(vFences[j]-vFences[i])
        common = diffs_a & diffs_b
        if common:
            ans =  max(common)*max(common)
            return ans % (10**9+7)

        return -1
        



        