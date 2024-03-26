class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Input: word = "aabcaba", k = 0
        Output: 3

        [1,2,4] 7-4 7-3
        Input: word = "dabdcbdcdcd", k = 2

        Output: 2
        [5,1,2,3]
        [1,2,3,5]
        # alaym it would take one year I will solve it.


        "
        sort counts and 
        think about two pointer 
        compare left and right
        right - left <= k:brek
        if that is not the case you have two choises either substract 1 from left or substract 1 from right and right should not be less than the value before it if it is going to be < the value before it we must subtract one from the left and if the left becomes 0 increment the left pointer.
        [1,2,3,5]
        """
        count = Counter(word)
        counter = [c for c in count.values()]
        ans = float(inf)
        pref= 0
        counter.sort()
        for i in range(len(counter)):
            temp = 0
            for j in range(i,len(counter)):
                if counter[j]-counter[i]>k:
                    temp+=counter[j]-counter[i]-k
            temp+=pref
            ans = min(ans,temp)
                


            pref += counter[i]
        return ans


        