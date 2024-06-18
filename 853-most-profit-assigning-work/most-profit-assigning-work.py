class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        """pre processing"""
        list_zip = list(zip(difficulty,profit))
        list_zip.sort()
        difficulty,profit = zip(*list_zip)
        worker.sort(reverse=True)
        profit = list(profit)

        """assume"""

        # assume as difficulty increases profit also increases, if you can afford the maximum difficulty you can surely afford the minimum difficulty,  so what stops you from taking the profit from the minimum difficulty while you can do a more difficult work, (let's assume again you are lazy :),so always choose an affordable maximum profit)
        max_so_far = 0
        for i,j in enumerate(difficulty):
            if max_so_far > profit[i]:
                profit[i] = max_so_far
            max_so_far = max(max_so_far,profit[i])


        # final

        ans = 0

        l = len(difficulty)-1
        for i in worker:
            while difficulty[l]>i and l>=0:
                l-=1
            if l<0:
                break
            ans+=profit[l]

        return ans
        