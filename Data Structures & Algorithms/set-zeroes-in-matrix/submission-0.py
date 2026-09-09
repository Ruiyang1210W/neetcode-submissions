class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix), len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # record which rows cols neet to be 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in range(r):
            for j in range(c):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
                    