class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(r,c):
            if (
                r not in range(rows) or c not in range(cols) or (r,c) in visited
                ):
                    return
            visited.add((r,c))
            neighbors = [(1,0),(0,-1),(-1,0),(0,1)]
            for a,b in neighbors:
                newr = a+r
                newc = b+c
                if newr not in range(rows) or newc not in range(cols) or (newr,newc)  in visited:
                    continue
                if board[newr][newc] != "O":
                    continue
                dfs(newr,newc)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 and board[r][c] == "O":
                    dfs(r,c)
                elif r == rows-1 and board[r][c] == "O":
                    dfs(r,c)
                elif c == 0 and board[r][c] == "O":
                    dfs(r,c)
                elif c == cols-1 and board[r][c] == "O":
                    dfs(r,c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in visited:
                    pass
                else:
                    board[i][j] = "X"
        return board
                                
        