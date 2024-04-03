class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        a up visited the take index and the next should be equal to the string at index
        a down visited
        a right visited
        a left visited
        """
        ans = False
        def dfs(idx,i,j,string,visited):
            nonlocal ans
            
            if idx == len(word):
              
                ans = True
                return True
            if (i,j) in visited:
                return 
            if i<0 or i>=len(board) or j< 0 or j>=len(board[0]):
                return 
            dirn = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in dirn:
                next_i,next_j = x+i,y+j
               
                if next_i<0 or next_i>=len(board) or next_j<0 or next_j>=len(board[0]) or (next_i,next_j) in visited:
                    continue
               
                if board[next_i][next_j] == word[idx]:
                    visited.append((i,j))
                    dfs(idx+1,next_i,next_j,string+board[next_i][next_j],visited)
                    visited.pop()
       
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(1,i,j,word[0],[])
        return ans
       


        