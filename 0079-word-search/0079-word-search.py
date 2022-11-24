class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ##
        R = len(board)
        C = len(board[0])
        
        # if len of word is greater than total number of character in board
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        # count of a LETTER in word is Greater than count of it being in board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        # if count of 1st letter of Word(A) is Greater than that of Last One in Board(B). 
        # Reverse Search the word then search as less case will be searched.
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
        
        ##
        
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtracking(i, j,word,board):
                    return True
        return False
    def backtracking(self,i, j,word,board):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            if board[i][j] == word[0]:
                board[i][j] = "~"
                if self.backtracking(i+1, j, word[1:],board) or self.backtracking(i-1, j, word[1:],board) or self.backtracking(i, j+1, word[1:],board) or self.backtracking( i, j-1, word[1:],board):
                    return True
                board[i][j] = word[0]
            return False