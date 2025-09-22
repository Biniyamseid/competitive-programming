class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # [1,2,3,4,5]
        # find maximum frequency
        # find numbers with maximum frequency
        #return their count or max frequency*count(frequnet numbers)

        # make a map of number to frequency
        # find the maximum frequency
        # find numbers with this maxfrequency 
        # multiple count with frequency

        frequency_map = {i:0 for i in nums}
        for num in nums:
            frequency_map[num]+=1
        max_frequency = max([j for i,j in frequency_map.items()])
        max_frequent_number_count = 0
        for i,j in frequency_map.items():
            if j == max_frequency:
                max_frequent_number_count += 1
        return max_frequency * max_frequent_number_count

        