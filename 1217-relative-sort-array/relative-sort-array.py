class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notinarrtwo = []
        se = set(arr2)
        for i in arr1:
            if i not in se:
                notinarrtwo.append(i)
        ans = []
        count = Counter(arr1)
        for i in arr2:
                ans.extend([i]*count[i])
        ans =  ans+sorted(notinarrtwo)
        return ans

        