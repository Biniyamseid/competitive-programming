class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_val = [[] for i in range(len(board[0])+1)]
        col_val = [[] for i in range(len(board)+1)]

        three_by_three = [[] for i in range(9)]

        # print(row_val,col_val,three_by_three)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                row_val[i].append(curr)
                col_val[j].append(curr)
                th_i = int(math.floor(i/3))
                th_j = int(math.floor(j/3))
                print("th_j",th_j,j,j/3,)
                th_index = int(n/3)*th_i+th_j
                print(th_index)
                three_by_three[th_index].append(curr)



        
        for i in row_val:
           
            if len(i)!=len(set(i)):
              
                return False
        for i in col_val:
            
            if len(i)!=len(set(i)):
                
                return False
        for i in three_by_three:
            
            if len(i)!=len(set(i)):
               
                return False
        return True

        