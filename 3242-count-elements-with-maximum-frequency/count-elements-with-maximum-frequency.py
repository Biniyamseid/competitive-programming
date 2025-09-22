class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        #
        total_frequency = 0
        max_frequency = 0
        frequency = {num:0 for num in nums }
        for num in nums:
            frequency[num]+=1
            current_frequency = frequency[num]
            
            
            if current_frequency > max_frequency:
                max_frequency = current_frequency
                total_frequency = max_frequency
            elif current_frequency == max_frequency:
                total_frequency += max_frequency
        return total_frequency
            


        # [1,2,3,4,5]
        # find maximum frequency
        # find numbers with maximum frequency
        #return their count or max frequency*count(frequnet numbers)

        # make a map of number to frequency
        # find the maximum frequency
        # find numbers with this maxfrequency 


        # frequency = [0]*100
        # for num in nums:
        #     frequency[num-1]+=1
        # frequency.sort()
        # max_freq = frequency[-1]
        # total_sum = 0
        # for freq in frequency[::-1]:
        #     if freq!= max_freq:
        #         break
        #     total_sum += freq

        # return total_sum


        # max_freq = 0
        # total_freq = 0
        # for num in nums:
        #     if num== max_freq:
        #         total_freq+=num
        #     if num > max_freq:
        #         max_freq = num
        #         total_freq = max_freq
        # return total_freq
        
        
     
        # return total_sum


        # # multiple count with frequency

        # frequency_map = {i:0 for i in nums}
        # for num in nums:
        #     frequency_map[num]+=1
        # max_frequency = max([j for i,j in frequency_map.items()])
        # max_frequent_number_count = 0
        # for i,j in frequency_map.items():
        #     if j == max_frequency:
        #         max_frequent_number_count += 1
        # return max_frequency * max_frequent_number_count

        