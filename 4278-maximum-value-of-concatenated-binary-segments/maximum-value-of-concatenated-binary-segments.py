class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        N = len(nums1)
        MOD = 10 ** 9 + 7
        ans = []

        h = [] # max heap
        for i in range(N):
            ones = nums1[i]
            zeroes = nums0[i]
            
            # edge case- only ones present
            if zeroes == 0:
                ans.append('1' * ones)
                continue

            heappush(h, (-ones, zeroes))

        while h:
            ones, zeroes = heappop(h)
            ones = -ones
            ans.append('1' * ones + '0' * zeroes)

        return int(''.join(ans), 2) % MOD