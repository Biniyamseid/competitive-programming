class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        "find the first positive number start ordering from it next find the second negative number"
        """split the array into two positive and negative and each time insert into the array from the arrays"""
        positive = []
        Negative = []
        answer = []
        for i in nums:
            if i>=0:
                positive.append(i)
            else:
                Negative.append(i)
        turn = True
        n = len(nums)
        j = 0 
        p=0
        ne=0
        while j<n:
            if turn:
                answer.append(positive[p])
                p+=1
            else:
                answer.append(Negative[ne])
                ne+=1
            turn = not turn
            j+=1
        return answer
        

        