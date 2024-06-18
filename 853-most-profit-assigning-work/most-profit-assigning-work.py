class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
        worker.sort(reverse=True)
        [7,6,5,4]
        l = len(diff)-1
        for i in worker:
            if diff[l]>i:
                l-=1
            else:
                ans+=diff[l]
            if l<0:
                break
        return ans
        """
        list_zip = list(zip(difficulty,profit))
        list_zip.sort()
       
        difficulty,profit = zip(*list_zip)
        
        profit = list(profit)
        max_so_far = 0
        for i,j in enumerate(difficulty):
            if max_so_far > profit[i]:
                profit[i] = max_so_far
            max_so_far = max(max_so_far,profit[i])

        ans = 0
        worker.sort(reverse=True)
        l = len(difficulty)-1
        for i in worker:
            while difficulty[l]>i and l>=0:
                l-=1
            if l<0:
                break
            
            ans+=profit[l]
        return ans
        