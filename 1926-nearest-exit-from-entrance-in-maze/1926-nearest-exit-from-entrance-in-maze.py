class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        [["+","+",".","+"]
        [".",".",".","+"]
        ["+","+","+","."]]
        
        entrance = [1,2]
        I will do depth first search starting from the entrance
        and I will put the steps from the entrance to the exit and
        return the minimum step
        
        don't count entrace as exit even if it is at the boarder.
        
        if there is no exit return -1.
        """
        result = []
        rows= len(maze)
        columns = len(maze[0])
        visited = set()
        
        def bfs(r,c,step):
            #visited.add((r,c))
            queue = deque([(r,c,0)])
            while queue:
                row,column,step = queue.popleft()
                if (row,column) in visited:
                    continue
                visited.add((row,column))
                if row<0 or row >= rows or column<0 or column>=columns:
                    if step != 1:
                        result.append(step)
                    continue
                if maze[row][column] == "+":
                    continue
                queue.append((row-1,column,step+1))
                queue.append((row+1,column,step+1))
                queue.append((row,column-1,step+1))
                queue.append((row,column+1,step+1))
                

        a,b = entrance
        bfs(a,b,0)
        print(result)
        if result:
            return min(result)-1
        return -1
    
#         def dfs(r,c,step):
            
#             if (r < 0) or  (r>= row) or (c<0) or (c >= column):
#                 if step != 1:
#                     result.append(step)
#                 return 0
#             if maze[r][c] == "+":
#                 return 0
#             if (r,c) in visited:
#                 return
#             visited.add((r,c))
#             dfs(r,c+1,step+1)
#             dfs(r,c-1,step+1)
#             dfs(r+1,c,step+1)
#             dfs(r-1,c,step+1)
#             visited.remove((r,c))
        
        
        
            
            
        
        