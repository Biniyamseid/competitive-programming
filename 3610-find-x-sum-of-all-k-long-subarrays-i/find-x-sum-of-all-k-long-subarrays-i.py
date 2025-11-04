from collections import  Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1):
            current_list = nums[i:i+k]
            count = Counter(current_list)
            most_common = sorted(
                count.items(),
            key=lambda item: (-item[1],-item[0]))[:x]
            sum_x = sum(number*freq for number,freq in most_common)
            answer.append(sum_x)


        return answer


        