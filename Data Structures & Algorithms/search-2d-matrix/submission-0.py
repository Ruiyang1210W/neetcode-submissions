class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        left = 0
        right = ROWS * COLS -1
        while left <= right:
            mid = (left + right) // 2

            # 把一维的 mid 翻译成矩阵里的具体物理位置
            row = mid // COLS
            col = mid % COLS

            current_num = matrix[row][col]

            if current_num == target:
                return True
            elif current_num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

