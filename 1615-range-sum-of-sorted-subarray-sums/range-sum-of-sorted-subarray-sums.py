class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        query_list = []
        for i in range(n):
            sums = 0
            
            for j in range(i,n):
                sums+=nums[j]

                query_list.append(sums)

        store_subarray = query_list

        store_subarray.sort()

        # Find the sum of all values between left and right.
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            range_sum = (range_sum + store_subarray[i]) % mod
        return range_sum
        query_list.sort()
        print(query_list)
        return sum(query_list[left-1:right])

        