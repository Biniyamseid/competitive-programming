import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        left = [-1] * n
        right = [-1] * n
        alive = [True] * n

        for i in range(n):
            if i > 0:
                left[i] = i - 1
            if i < n - 1:
                right[i] = i + 1

        # count bad (decreasing) adjacent pairs
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            # get valid minimum-sum pair
            while True:
                s, i = heapq.heappop(heap)
                j = right[i]
                if j != -1 and alive[i] and alive[j] and nums[i] + nums[j] == s:
                    break

            li = left[i]
            rj = right[j]

            # remove old violations
            if li != -1 and nums[li] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if rj != -1 and nums[j] > nums[rj]:
                bad -= 1

            # merge
            nums[i] += nums[j]
            alive[j] = False
            right[i] = rj
            if rj != -1:
                left[rj] = i

            # add new violations
            if li != -1 and nums[li] > nums[i]:
                bad += 1
            if rj != -1 and nums[i] > nums[rj]:
                bad += 1

            # push new adjacent sums
            if li != -1:
                heapq.heappush(heap, (nums[li] + nums[i], li))
            if rj != -1:
                heapq.heappush(heap, (nums[i] + nums[rj], i))

            ops += 1

        return ops
