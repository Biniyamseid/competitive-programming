class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [ i for i in arr if len(set(i))==len(i)]
        if len(arr)==0: return 0
        maxm = 0
        def backt(i,visited):
            nonlocal maxm
            if i>=len(arr):
                return
            duplicate = False
            vis = "".join(visited)
           
            for j in arr[i]:
                if j in vis:
                    duplicate = True
            if duplicate:
                backt(i+1,visited)
            else:
                visited.append(arr[i])
                vis = "".join(visited)
                maxm = max(maxm,len(vis))
                backt(i+1,visited)
                visited.pop()
                backt(i+1,visited)
            maxm = max(maxm,len(vis))
        backt(0,[])
        return maxm

        