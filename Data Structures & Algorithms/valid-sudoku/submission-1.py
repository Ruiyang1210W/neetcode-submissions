class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # bit mask
        # Create three arrays of size 9:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        # Loop through each cell (r, c) of the board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]: # << Bitwise Left Shift
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c//3)] |= (1 << val)

                # & 与 |=（查重与登记）
            
        return True