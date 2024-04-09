class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0     
        target = tickets[k]
        print(target)
        for tick in tickets:
            if tick<=target:
                ans+=tick
            else:
                ans+=target
        deduc = 0
        for j in range(k+1,len(tickets)):
            if tickets[j]>=target:
                deduc+=1
        return ans - deduc


        