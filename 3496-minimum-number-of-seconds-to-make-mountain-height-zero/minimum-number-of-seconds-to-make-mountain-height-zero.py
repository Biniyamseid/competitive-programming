import heapq
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, t, 1) for i, t in enumerate(workerTimes)]
        heapify(h)
        while mountainHeight > 1:
            ps, wt, x = heappop(h)
            heappush(h, (ps + wt * (x + 1), wt, x + 1))
            mountainHeight-= 1
        return heappop(h)[0] 
        # heap = []
        # heapq.heapify(heap)
        # for idx,i in enumerate(workerTimes):
        #     heapq.heappush(heap,(i,i,1,idx,i))
        # while mountainHeight > 1:
        #     mn,m,n,idx,ans = heapq.heappop(heap)
        #     heapq.heappush(heap,(mn+m*(n+1),m,n+1,idx,ans+ ans*(n+1)))
        #     mountainHeight-=1
        # return heapq.heappop(heap)[0]


        

        time = defaultdict(int)
        counter= defaultdict(int)
        sec = 0
        heap = []
        heapq.heapify(heap)
        for idx,i in enumerate(workerTimes):
            heapq.heappush(heap,(i,i,1,idx,i))
        while mountainHeight > 1:
            # print("heap")
            print(heap)
            mn,m,n,idx,ans = heapq.heappop(heap)
            # print("mn,m,n,idx")
            
            print(mn,m,n,"mountiainheign",mountainHeight)
            
            sec += 1
            mountainHeight-=1
            heapq.heappush(heap,(m*(n+1),m,n+1,idx,ans+ ans*(n+1)))
            
            print("mn")
            print(mn)
            time[idx]+=mn
            counter[idx]+=1
            
            print((m*(n+1),m,n+1))
            print(" ")
        print("counter")
        print(counter)
        ans = 0
        print(time)
        print("time")
        for key in time:
            ans = max(time[key],ans)
        print("heap",heap)
        ans = float(inf)
        for i,j,k,l,m in heap:
            ans = min(ans,m)
        return ans
        
        