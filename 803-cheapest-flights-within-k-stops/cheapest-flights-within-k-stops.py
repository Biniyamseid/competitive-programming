class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float(inf) for j in range(n)]
        prices[src] = 0
        for i in range(k+1):
            curr = prices.copy()
            for s,d,p in flights:
                if prices[s]==float(inf):
                    continue
                if prices[s]+p <curr[d]:
                    curr[d] = prices[s]+p
            prices = curr
        print(prices)
        if prices[dst]==float(inf):prices[dst]=-1
        return prices[dst]

        