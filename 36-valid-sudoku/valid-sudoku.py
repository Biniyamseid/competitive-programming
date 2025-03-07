class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_val = [set() for i in range(len(board[0])+1)]
        col_val = [set() for i in range(len(board)+1)]

        three_by_three = [set() for i in range(9)]

        # print(row_val,col_val,three_by_three)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                
                if curr == ".":
                    continue
                th_i = int(math.floor(i/3))
                th_j = int(math.floor(j/3))
                print("th_j",th_j,j,j/3,)
                th_index = int(n/3)*th_i+th_j
                if curr in row_val[i] or curr in col_val[j] or curr in three_by_three[th_index]:
                    return False
                row_val[i].add(curr)
                col_val[j].add(curr)
                three_by_three[th_index].add(curr)

        return True

        