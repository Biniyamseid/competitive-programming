class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        bitormap = defaultdict(int)
        for i in range(1001):
            result = i | i+1
            if bitormap[result]==-0:
                bitormap[result] = i
        answer = []
        for i in nums:
                if bitormap[i] == 0:
                    answer.append(-1)
                else:
                    answer.append(bitormap[i])
        return answer
            