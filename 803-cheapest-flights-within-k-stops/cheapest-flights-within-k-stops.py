class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float(inf) for i in range(n)]
        prices[src] = 0
        for i in range(k+1):
            curr = prices.copy()
            for src,d,p in flights:
                if prices[src]==float(inf):
                    continue
                if prices[src]+p <curr[d]:
                    curr[d] = prices[src]+p
            prices = curr
        return prices[dst] if prices[dst]!=float(inf) else -1
        """

        prices = [float(inf) for i in range(n)]
        prices[src] = 0
        for i in range(k+1):
            curr = 
                    

        """
        