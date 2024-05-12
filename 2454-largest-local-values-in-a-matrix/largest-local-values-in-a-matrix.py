class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                # print(curr)
        """
        0,0 0,1 0,2  0,1 0,2 0,3  0,2 0,3 0,4    
        1,           
        2,0  2,1 2,2  

        """
        k = 0
        # 0,0 0,1 0,2
        # 1,0 1,1 1,1
        # 2,0 2,1 2,2


        # 0,1 0,2 0,3
        # 1,1 1,2 1,3
        # 2,1 2,2 2,3
        answer = []
        for i in range(len(grid)):
         for sk in range(len(grid[0])):
            # 0,1,2,3
            # 0,1,2
            print(i,"IIII")
            mx = float(-inf)
            flag = True
            for l in range(i,i+3):
                # print(i,j)
                for j in range(sk,sk+3):
                    print(l,j)
                    if l<len(grid) and j<len(grid[0]):
                        mx = max(mx,grid[l][j])
                    else:
                        
                        flag= False
        
            if not flag:
                    continue
            answer.append(mx)
        N = len(grid)
        n_size = N-2
        ans = [[0]*n_size for i in range(n_size)]
        k = 0
        for i in range(len(ans)):
            for j in range(len(ans)):
                ans[i][j] = answer[k]
                k+=1
        return ans


        


        