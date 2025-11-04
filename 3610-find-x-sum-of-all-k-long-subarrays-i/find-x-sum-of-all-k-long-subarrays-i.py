from collections import  Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1):
            current_list = nums[i:i+k]
            print(current_list)
            count = Counter(current_list)
            most_common = sorted(
                count.items(),
            key=lambda item: (-item[1],-item[0]))[:x]
            sum_x = 0
            print(most_common)
            for number,freq in most_common:
                current_sum = number*freq
                sum_x+=current_sum
            answer.append(sum_x)


        return answer


        