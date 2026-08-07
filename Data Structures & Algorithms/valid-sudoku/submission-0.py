class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            myHash = {}
            for num in range(9):
                val = board[row][num]
                if val == '.': 
                    continue
                if val in myHash: 
                    return False
                myHash[val] = True
                
        for col in range(9):
            myHash = {}
            for num in range(9):
                val = board[num][col] 
                if val == '.': continue
                if val in myHash: return False
                myHash[val] = True
        

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                myHash = {}
                for r in range(3):
                    for c in range(3):
                        val = board[box_row + r][box_col + c]
                        if val == '.': continue
                        if val in myHash: return False
                        myHash[val] = True
                        
        return True
