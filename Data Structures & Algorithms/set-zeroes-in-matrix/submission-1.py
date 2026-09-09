class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix), len(matrix[0])
        first_r_zero = any(matrix[0][j] == 0 for j in range(c))
        first_c_zero = any(matrix[i][0] == 0 for i in range(r))

        #用第一行第一列记录内部元素是否为0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据第一行第一列标记更新内部
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第一行和第一列
        if first_r_zero:
            for j in range(c):
                matrix[0][j] = 0
        
        if first_c_zero:
            for i in range(r):
                matrix[i][0] = 0        