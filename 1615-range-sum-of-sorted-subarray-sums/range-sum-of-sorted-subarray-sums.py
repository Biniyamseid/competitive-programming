class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        query_list = []
        for i in range(n):
            sums = 0
            for j in range(i,n):
                sums+=nums[j]
                query_list.append(sums)
        query_list.sort()
        print(query_list)
        return sum(query_list[left-1:right])%mod

        